import logging
from datetime import timedelta
from os.path import exists
from typing import Optional

from django.utils import timezone

from api.models import EmailNotificationTemplate, Notification, User
from api.models.notification import EmailNotificationTemplateEnum
from api.models.status import UserEnum
from api.models.user.onboarding import onboarding_components

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
logger.setLevel(logging.INFO)


def _find_target_users():
    now = timezone.now()
    half_hour_ago = now - timedelta(hours=0.5)
    three_hours_ago = now - timedelta(hours=3)

    signed_up_an_hour_ago = User.objects.filter(
        date_joined__range=(three_hours_ago, half_hour_ago),
    )

    ten_days_ago = now - timedelta(days=10)
    ten_days_and_three_hours_ago = now - timedelta(days=10, hours=3)

    now_completed = User.objects.filter(
        date_joined__range=(ten_days_and_three_hours_ago, ten_days_ago),
    )

    return list(signed_up_an_hour_ago) + list(now_completed)


def _determine_template(user: User) -> Optional[str]:
    if user.status == UserEnum.ONBOARDING.value:
        onboarding_status = user.get_onboarding_status()
        missing_fields = onboarding_status["missing_fields"]
        if (
            user.service_agreements.all().exists()
            and onboarding_components.CONFIRM_PROVIDERS in missing_fields
        ):
            return EmailNotificationTemplateEnum.cs_no_confirmation.value

        if (
            missing_fields[0] == onboarding_components.PHONE_NUMBER
            or missing_fields[0] == onboarding_components.EMAIL
        ):
            return EmailNotificationTemplateEnum.cs_no_verification.value

        if user.gmail_processing_tasks.filter(failed=True).exists():
            return EmailNotificationTemplateEnum.cs_gmail_permissions.value

        if not user.service_agreements.all().exists():
            return EmailNotificationTemplateEnum.cs_no_providers_selected.value

    if user.status == UserEnum.IN_REVIEW.value:
        first_address = user.addresses.all()[0]
        second_address = user.addresses.all()[1]

        if (
            first_address.postcode == second_address.postcode
            and first_address.address_lines == second_address.address_lines
        ):
            return EmailNotificationTemplateEnum.cs_same_address.value

    if user.status == UserEnum.MOVING.value:
        ten_days_ago = timezone.now() - timedelta(days=10)
        if user.date_joined < ten_days_ago:
            return EmailNotificationTemplateEnum.cs_one_week_update.value

    return None


def _handle_side_effects(user, template_name):
    if template_name == EmailNotificationTemplateEnum.cs_gmail_permissions.value:
        user.delete()


def run_mail_sending_job(target_users=None, is_event=True):
    # Shouldn't work now since emails are hashed
    users = target_users
    if target_users is None or is_event:
        users = _find_target_users()
    for user in users:
        template_name = _determine_template(user)
        if (
            template_name is None
            or user.notifications.filter(
                email_template__name=template_name
            ).exists()  # NO double send
        ):
            continue
        template = EmailNotificationTemplate.objects.filter(name=template_name).first()

        logger.debug("Sending template %s to user %s", template, user.email)
        notification = Notification.create_user_email_notification(
            user=user, template=template,
        )
        notification.send()
        notification.save()
        _handle_side_effects(user, template_name)

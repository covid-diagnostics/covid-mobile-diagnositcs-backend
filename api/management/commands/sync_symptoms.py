from django.core.management.base import BaseCommand, CommandError
import json

from api.models import Question
from api.models.question import QuestionType

ICON_URL = "https://staging-storage-corona-testing.s3-eu-west-1.amazonaws.com/media/symptom-icons/{name}.svg"
SYMPTOMS = [
    {"name_en": "Cough", "name_he": "שיעול", "optionValue": "cough"},
    {"name_en": "Body ache", "name_he": "כאבי גוף", "optionValue": "body_ache"},
    {"name_en": "Cold sweat", "name_he": "זיעה קרה", "optionValue": "cold_sweat"},
    {"name_en": "Diarrhea", "name_he": "שילשול", "optionValue": "diarrhea"},
    {"name_en": "Dizziness", "name_he": "סחרחורת", "optionValue": "dizziness"},
    {
        "name_en": "Eye inflammation",
        "name_he": "דלקת עיניים",
        "optionValue": "eye_inflammation",
    },
    {"name_en": "Fever", "name_he": "חום", "optionValue": "fever"},
    {"name_en": "Headache", "name_he": "כאב ראש", "optionValue": "headache"},
    {
        "name_en": "Loss of flavour",
        "name_he": "אבדן חוש טעם",
        "optionValue": "loss_of_flavour",
    },
    {
        "name_en": "Loss of smell",
        "name_he": "אבדן חוש ריח",
        "optionValue": "loss_of_smell",
    },
    {
        "name_en": "Loss of appetite",
        "name_he": "חוסר תיאבון",
        "optionValue": "low_appetite",
    },
    {"name_en": "Nausea", "name_he": "בחילה", "optionValue": "nausea"},
    {"name_en": "Rash", "name_he": "פריחה", "optionValue": "rash"},
    {"name_en": "Stomach ache", "name_he": "כאב בטן", "optionValue": "stomache_ache"},
    {"name_en": "Throat ache", "name_he": "כאב גרון", "optionValue": "throat_ache"},
    {"name_en": "Tiredness", "name_he": "עייפות", "optionValue": "tiredness"},
]


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        symp_question, created = Question.objects.get_or_create(
            name="symptoms",
            display_name_en="What symptoms do you have?",
            display_name_he="מה הסימפטומים שלך?",
            qtype=QuestionType.MULTISELECT.value,
            order=1,
        )

        symp_question.extra_data_en = json.dumps(
            [
                {
                    "optionName": symp["name_en"],
                    "optionValue": symp["optionValue"],
                    "optionImage": ICON_URL.format(name=symp["optionValue"]),
                }
                for symp in SYMPTOMS
            ]
        )

        symp_question.extra_data_he = json.dumps(
            [
                {
                    "optionName": symp["name_he"],
                    "optionValue": symp["optionValue"],
                    "optionImage": ICON_URL.format(name=symp["optionValue"]),
                }
                for symp in SYMPTOMS
            ]
        )

        symp_question.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully updates %s symptoms" % len(SYMPTOMS))
        )

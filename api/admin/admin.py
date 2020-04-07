# pylint: disable=missing-docstring
"""Admin page registration"""
import csv

from django.apps import apps
from django.contrib import admin
from django.utils.functional import cached_property
from django.http import HttpResponse

from .input_filters import *
from api.models import AnonymousMetrics


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        property_names = [
            name
            for name in dir(self.model)
            if name not in field_names
            and (
                isinstance(getattr(self.model, name), property)
                or isinstance(getattr(self.model, name), cached_property)
            )
        ]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names + property_names)
        for obj in queryset:
            writer.writerow(
                [getattr(obj, field) for field in field_names + property_names]
            )

        return response

    export_as_csv.short_description = "Export Selected As CSV"  # type: ignore


class CustomAdmin(admin.ModelAdmin, ExportCsvMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.actions:
            self.actions = ["export_as_csv"]
        else:
            self.actions.append("export_as_csv")


class AnonymousMetricsAdmin(CustomAdmin, admin.ModelAdmin):
    list_display = ("filled_on", "app_heart_rate", "device_heart_rate", "heart_rate_diff",
                    "app_saturation", "device_saturation", "saturation_diff",
                    "device_type", "measurement_method", "lightning", "age")
    list_filter = ("filled_on", AppHeartRateFilter, DeviceHeartRateFilter, HeartRateDiffFilter,
                   AppSaturationFilter, DeviceSaturationFilter, SaturationDiffFilter,
                   "device_type", "measurement_method", "lightning", AgeFilter)


admin.site.register(AnonymousMetrics, AnonymousMetricsAdmin)

app_models = apps.get_app_config("api").get_models()  # pylint: disable=invalid-name
for model in app_models:
    try:
        admin.site.register(model, CustomAdmin)
    except admin.sites.AlreadyRegistered:
        pass

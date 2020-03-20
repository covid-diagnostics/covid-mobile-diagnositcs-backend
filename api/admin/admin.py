# pylint: disable=missing-docstring
"""Admin page registration"""
import csv
import uuid

from django.apps import apps
from django.contrib import admin
from django.utils.functional import cached_property
from django.http import HttpResponse


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


app_models = apps.get_app_config("api").get_models()  # pylint: disable=invalid-name
for model in app_models:
    try:
        admin.site.register(model, CustomAdmin)
    except admin.sites.AlreadyRegistered:
        pass

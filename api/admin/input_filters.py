from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def __init__(self, *args, **kwargs):
        super(InputFilter, self).__init__(*args, **kwargs)

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

    @staticmethod
    def get_value_range(value):
        if not value:
            return None
        return [int(n.strip("' ")) if n.strip("' ") != 'None' else None
                for n in value.strip(
                '[]').split('-')]

    def queryset(self, request, queryset):
        term = self.value()
        if term is None:
            return
        values_range = self.get_value_range(term)
        if not values_range:
            return queryset
        min_val, max_val = values_range
        if min_val and max_val:
            query = {'%s__range' % self.parameter_name:
                         (min_val, max_val)}
        elif min_val:
            query = {'%s__gt' % self.parameter_name: min_val}
        elif max_val:
            query = {'%s__lt' % self.parameter_name: max_val}
        else:
            query = {}
        return queryset.filter(**query)


class AppHeartRateFilter(InputFilter):
    parameter_name = 'app_heart_rate'
    title = _('App Heart Rate')


class DeviceHeartRateFilter(InputFilter):
    parameter_name = 'device_heart_rate'
    title = _('Device Heart Rate')


class HeartRateDiffFilter(InputFilter):
    parameter_name = 'heart_rate_diff'
    title = _('Heart Rate Diff')


class AppSaturationFilter(InputFilter):
    parameter_name = 'app_saturation'
    title = _('App Saturation')


class DeviceSaturationFilter(InputFilter):
    parameter_name = 'device_saturation'
    title = _('Device Saturation')


class SaturationDiffFilter(InputFilter):
    parameter_name = 'saturation_diff'
    title = _('Saturation Diff')


class AgeFilter(InputFilter):
    parameter_name = 'age'
    title = _('Age')

from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin

from ..admin_site import cancer_prn_admin
from ..forms import SubjectDeathForm
from ..models import DeathReport


@admin.register(DeathReport, site=cancer_prn_admin)
class DeathRportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectDeathForm

    fieldsets = (
        (None, {
            'fields': (
                "subject_identifier",
                "death_date",
                "is_death_date_estimated",
                'cause',
                "cause_other",
                "death_cause",
                "cause_category",
                "cause_category_other",
                "participant_hospitalized",
                "reason_hospitalized",
                "reason_hospitalized_other",
                "days_hospitalized",
                "comment",
                "illness_duration",
                "perform_autopsy",
                "diagnosis_code",
                "diagnosis_code_other",
                "medical_responsibility"
            )}),
        audit_fieldset_tuple
    )
    radio_fields = {
        'is_death_date_estimated': admin.VERTICAL,
        'participant_hospitalized': admin.VERTICAL,
        'perform_autopsy': admin.VERTICAL,
    }

    list_display = ('subject_identifier', 'death_date')

    filter_horizontal = ('cause', 'medical_responsibility', 'diagnosis_code',
                         'reason_hospitalized')


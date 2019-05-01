from datetime import datetime, time
from django.db import models
from edc_base.model_fields import IsDateEstimatedField
from edc_death_report.model_mixins import DeathReportModelMixin
from edc_identifier.model_mixins import UniqueSubjectIdentifierModelMixin
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_death_report.models import (
    Cause, CauseCategory, ReasonHospitalized,
    DiagnosisCode, MedicalResponsibility)


class DeathReport(DeathReportModelMixin,
                   UniqueSubjectIdentifierModelMixin,
                   SiteModelMixin, BaseUuidModel):

    is_death_date_estimated = IsDateEstimatedField(
        verbose_name="Is date of death estimated?",
        null=True,
        blank=False,
    )
    cause = models.ManyToManyField(
        Cause,
        verbose_name=(
            'What is the primary source of cause of death information? '
            '(if multiple source of information, '
            'list one with the smallest number closest to the top of the list) '))

    cause_category = models.ManyToManyField(
        CauseCategory,
        verbose_name=("Based on the above description, what category "
                      "best defines the major cause of death? "),
        help_text="")

    reason_hospitalized = models.ManyToManyField(
        ReasonHospitalized,
        verbose_name="if yes, hospitalized, what was the primary reason for hospitalisation? ",
        help_text="",
        blank=True)

    diagnosis_code = models.ManyToManyField(
        DiagnosisCode,
        max_length=25,
        verbose_name="Please code the cause of death as one of the following:",
        help_text="Use diagnosis code from Diagnosis Reference Listing")

    medical_responsibility = models.ManyToManyField(
        MedicalResponsibility,
        verbose_name=(
            "Who was responsible for primary medical care of the "
            "participant during the month prior to death?"),
        help_text="")

    def get_report_datetime(self):
        return datetime.combine(self.death_date, time(0, 0))

    class Meta:
        app_label = "cancer_prn"
        verbose_name = "Subject Death"

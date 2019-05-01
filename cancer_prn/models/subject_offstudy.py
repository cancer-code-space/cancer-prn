from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_base.model_fields.custom_fields import OtherCharField
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_base.model_validators import date_not_future
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_protocol.validators import date_not_before_study_start
from edc_protocol.validators import datetime_not_before_study_start
from cancer_subject.models.onschedule import OnSchedule
from edc_offstudy.choices import OFF_STUDY_REASONS
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins.off_schedule_model_mixin import (
    OffScheduleModelMixin)


class SubjectOffstudy(OffScheduleModelMixin, BaseUuidModel):

    """A model completed by the user that completed when the
    subject is taken off-study.
    """

    offstudy_date = models.DateField(
        verbose_name="Off-study Date",
        null=True,
        default=get_utcnow,
        validators=[
            date_not_before_study_start,
            date_not_future])

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        null=True,
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    reason = models.CharField(
        verbose_name="Please code the primary reason participant taken off-study",
        max_length=115,
        choices=OFF_STUDY_REASONS,
        null=True)

    reason_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment",
        blank=True,
        null=True)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def take_off_schedule(self):
        on_schedule = OnSchedule
        try:
            on_schedule_obj = on_schedule.objects.get(
                subject_identifier=self.subject_identifier)
        except on_schedule.DoesNotExist:
            pass
        else:
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                onschedule_model=on_schedule._meta.label_lower)
            schedule.take_off_schedule(offschedule_model_obj=self)

    class Meta:
        app_label = "cancer_prn"
        verbose_name_plural = "Subject Off Study"

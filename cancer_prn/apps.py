from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style
from cancer_prn import settings
style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'cancer_prn'
    verbose_name = 'Cancer prn'
    admin_site_name = 'cancer_prn_admin'

    def ready(self):
        from .models import study_termination_conclusion_on_post_save


if settings.APP_NAME == 'cancer_prn':
    from edc_visit_tracking.apps import (
        AppConfig as BaseEdcVisitTrackingAppConfig)
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_appointment.appointment_config import AppointmentConfig

#     class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
#         visit_models = {
#             'cancer_subject': ('subject_visit', 'cancer_subject.subjectvisit')}

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='cancer_subject.subjectvisit')
        ]

from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'cancer_prn'
    verbose_name = 'Cancer prn'
    admin_site_name = 'cancer_prn_admin'

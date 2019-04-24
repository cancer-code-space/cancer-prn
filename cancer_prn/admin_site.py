from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):

    site_url = '/administration/'


cancer_prn_admin = AdminSite(name='td_prn_admin')

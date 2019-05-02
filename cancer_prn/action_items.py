from edc_action_item import Action, HIGH_PRIORITY, site_action_items


DEATH_REPORT_ACTION = 'submit-death-report'

class DeathReportAction(Action):
    name = DEATH_REPORT_ACTION
    display_name = 'Submit Death Report'
    reference_model = 'cancer_prn.deathreport'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'cancer_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True

site_action_items.register(DeathReportAction)

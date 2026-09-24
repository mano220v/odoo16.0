from odoo import api, SUPERUSER_ID


def uninstall_hook(cr, registry):
    """Remove addon settings; Google-side consent must be revoked by the user."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["ir.config_parameter"].sudo().search([("key", "in", [
        "ow_gmail_inbox.client_id", "ow_gmail_inbox.client_secret", "ow_gmail_inbox.base_url",
    ])]).unlink()

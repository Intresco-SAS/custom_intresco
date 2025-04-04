
from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'account.tax'
    _description = 'Account Tax'

    x_tax_code = fields.Char(string='Código', required=True)
    
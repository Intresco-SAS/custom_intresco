# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    need_documentation = fields.Boolean(string='Need Documentation')
    contact_id = fields.Many2one('res.partner', string='Contact')
    mobile = fields.Char(related='contact_id.mobile', string='Mobile')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            for related_partner in self.partner_id.child_ids:
                if related_partner.type == 'contact':
                    self.contact_id = related_partner.id
                    break
        else:
            self.contact_id = False
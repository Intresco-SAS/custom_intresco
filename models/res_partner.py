from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    odoo_version = fields.Char(string='Odoo Version')
    active_customer = fields.Boolean(string='Active Customer')
    is_enterprise = fields.Boolean(string='Is Enterprise')
    rut_attachment = fields.Binary(string='RUT Attachment')
    cc_attachment = fields.Binary(string='Camara de Comercio Attachment')
    rut_attachment_filename = fields.Char(string='RUT Attachment Filename')
    cc_attachment_filename = fields.Char(string='Camara de Comercio Attachment Filename')
    server_url = fields.Char(string='Server URL')
    db_name = fields.Char(string='DB Name')
    user_qty = fields.Integer(string='User Quantity')
    contract_attachment = fields.Binary(string='Contract Attachment')
    contract_attachment_filename = fields.Char(string='Contract Attachment Filename')
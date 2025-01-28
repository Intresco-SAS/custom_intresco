from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OdooVersion(models.Model):
    _name = 'odoo.version'
    _description = 'Odoo Version'
    _sql_constraints = [
        ('version_unique', 'unique(version, odoo_version_type)', 'Ya existe una versión con ese número y tipo de versión')
    ]

    name = fields.Char(string='Name', compute = '_compute_name')
    version = fields.Char(string='Version')
    odoo_version_type = fields.Selection([
        ('community', 'Community'),
        ('enterprise', 'Enterprise')
    ], string='Odoo Version Type', required=True, default='community')

    @api.depends('version', 'odoo_version_type')
    def _compute_name(self):
        for record in self:
            record.name = "Odoo" + record.version + ' - ' + record.odoo_version_type.capitalize()
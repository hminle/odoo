from odoo import fields, models


class EquipmentManagement(models.Model):
    _inherit = 'maintenance.equipment'
    is_returned = fields.Boolean('Is Returned?')
    return_date = fields.Date('Expected Return Date')

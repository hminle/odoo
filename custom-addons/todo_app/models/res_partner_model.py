from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    todoo_ids = fields.Many2many(
        'todo.task',
        string='To-do Teams'
    )

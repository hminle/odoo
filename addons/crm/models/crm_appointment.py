# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Appointments(models.Model):

    _name = "crm.appointment"
    _description = "Appointments"
    _rec_name = 'id'
    _order = "id"

    partner_id = fields.Many2one('res.partner', string='Customer', Index=True)
    is_approved = fields.Boolean('Is Appointment approved')
    appointment_with = fields.Text('Has appointment with who')
    appointment_date = fields.Date('Date of Appointment', index=True)



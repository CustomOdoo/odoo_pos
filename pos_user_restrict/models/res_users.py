# -*- coding: utf-8 -*-

from odoo import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    pos_config_ids = fields.Many2many('pos.config', string='Available POS', help="Available POS for users. POS managers can view all POS configs.")

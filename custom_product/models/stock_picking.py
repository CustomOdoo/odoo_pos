from odoo import models, api, fields, _


class Picking(models.Model):
    _inherit = 'stock.picking'

    vendor_ref = fields.Char('Vendor Reference') 
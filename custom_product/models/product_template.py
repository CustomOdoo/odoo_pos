# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError


class CustomProductTemplate(models.Model):
	_inherit = 'product.template'

	def _get_default_uom_id(self):
		return self.env["product.uom"].search([], limit=1, order='id').id

	product_tag = fields.Selection([('Local', 'Local'), ('Dynamix', 'Dynamix')], string='Local / Dynamix')
	packing_size = fields.Char('Packing Size')
	uom_pos_id = fields.Many2one(
        'product.uom', 'Unit of Measure for POS',
        default=_get_default_uom_id, required=True,
        help="Default Unit of Measure used for all stock operation.")
	barcode = fields.Char('Barcode')

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError


class CustomProductTag(models.Model):
    _name = 'custom.product.tag'
    _description = 'Product Tag'

    name = fields.Char('Tag Name', required=True, translate=True)


class CustomProductTemplate(models.Model):
	_inherit = 'product.template'

	def _get_default_uom_id(self):
		return self.env["product.uom"].search([], limit=1, order='id').id

	product_tag = fields.Many2one('custom.product.tag',string='Local / Dynamix')
	packing_size = fields.Char('Packing Size')
	# list_price = fields.Float(string="Wholesale Price")
	# uom_id = fields.Many2one(string="Units/Case for sale")
	# uom_po_id = fields.Many2one(string="Units/Case")
	# type = fields.Selection(default='product')
	uom_pos_id = fields.Many2one(
        'product.uom', 'Unit of Measure for POS',
        default=_get_default_uom_id, required=True,
        help="Default Unit of Measure used for all stock operation.")

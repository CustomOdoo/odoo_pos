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

	product_tag = fields.Many2one('custom.product.tag',string='Local / Dynamix')
	packing_size = fields.Char('Packing Size')
	# requisition_price = fields.Float('Requisition Price', 
	# 							digits=dp.get_precision('Product Price'), 
	# 							help="Requisition price.")
	list_price = fields.Float(string="Wholesale Price")
	uom_id = fields.Many2one(string="Units/Case for sale")
	uom_po_id = fields.Many2one(string="Units/Case")
	# type = fields.Selection(default='product')

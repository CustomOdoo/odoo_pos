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

	product_tag = fields.Many2one('custom.product.tag',string='Product Tag')
	packing_size = fields.Char('Packing Size')
	whole_sale_price = fields.Float('Whole Sale Price', 
								digits=dp.get_precision('Product Price'), 
								help="Whole Sale price.")
	requisition_price = fields.Float('Requisition Price', 
								digits=dp.get_precision('Product Price'), 
								help="Requisition price.")

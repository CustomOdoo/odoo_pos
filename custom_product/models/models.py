# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomProductType(models.Model):
    _name = 'custom.product.type'
    _description = 'Product Type'

    name = fields.Char('Name', required=True, translate=True)


class CustomProduct(models.Model):
	_inherit = 'product.product'

	barcode = fields.Char('SKU')
	custom_product_type = fields.Many2one('custom.product.type', string='Custom Product Type')


# class CustomProductPackaging(models.Model):
# 	_inherit = 'product.packaging'

# 	case_price = fields.Float(
#         'Case Price', compute='_compute_product_price',
#         digits=dp.get_precision('Case Price'), inverse='_set_product_price')
# 	unit_price = fields.Float()
# 	whole_sale_price = fields.Float()
# 	retail_price = fields.Float()
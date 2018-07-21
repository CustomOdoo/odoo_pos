# -*- coding: utf-8 -*-
from odoo.addons import decimal_precision as dp
from odoo import models, fields, api


class CustomRetailPrice(models.Model):
	_inherit = 'product.template'

	retail_price = fields.Float('Retail Price', 
								digits=dp.get_precision('Product Price'), 
								help="Retail price.")
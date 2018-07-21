# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class product_tags(models.Model):
	_name = 'product.tags'
	
	name = fields.Char(string="Tag Name",required="1")
	
class product_template(models.Model):
    _inherit = 'product.template'
    
    tag_ids = fields.Many2one('product.tags',string='Where From?')
	

	




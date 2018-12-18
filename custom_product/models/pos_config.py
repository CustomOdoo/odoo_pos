# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import uuid

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class PosConfig(models.Model):
    _inherit = 'pos.config'

    pricelist_id = fields.Many2one('product.pricelist', string='Default Pricelist', required=True,
        help="The pricelist used if no customer is selected or if the customer has no Sale Pricelist configured.")
    available_pricelist_ids = fields.Many2many('product.pricelist', string='Available Pricelists', required=True,
        help="Make several pricelists available in the Point of Sale. You can also apply a pricelist to specific customers from their contact form (in Sales tab). To be valid, this pricelist must be listed here as an available pricelist. Otherwise the default pricelist will apply.")
    use_pricelist = fields.Boolean("Use a pricelist.", default=True)

    @api.onchange('use_pricelist')
    def _onchange_use_pricelist(self):
        """
        If the 'pricelist' box is unchecked, we reset the pricelist_id to stop
        using a pricelist for this posbox. 
        """
        if self.use_pricelist:
            self.update({
                'group_sale_pricelist': False,
                'group_pricelist_item': False,
            })
        if self.available_pricelist_ids == self._default_pricelist():
        	raise ValidationError("Please choose another pricelist")

    @api.onchange('available_pricelist_ids')
    def _onchange_available_pricelist_ids(self):
        if self.pricelist_id not in self.available_pricelist_ids:
            self.pricelist_id = False
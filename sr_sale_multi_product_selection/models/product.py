# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2017-Today Sitaram
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from odoo import fields, models, api


class SrCreateQuotation(models.TransientModel):
    _name = "sr.create.quotation"

    partner_id = fields.Many2one('res.partner', string="Partner")

    @api.multi
    def create_quotation(self):
        sale_id = self.env['sale.order'].create({'partner_id': self.partner_id.id})
        for product in self._context.get('active_ids'):
            self.env['sale.order.line'].create({'product_id': product,
                                                'order_id': sale_id.id})

        action = self.env.ref('sale.action_quotations').read()[0]
        action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
        action['res_id'] = sale_id.ids[0]
        return action

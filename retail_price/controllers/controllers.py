# -*- coding: utf-8 -*-
from odoo import http

# class RetailPrice(http.Controller):
#     @http.route('/retail_price/retail_price/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/retail_price/retail_price/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('retail_price.listing', {
#             'root': '/retail_price/retail_price',
#             'objects': http.request.env['retail_price.retail_price'].search([]),
#         })

#     @http.route('/retail_price/retail_price/objects/<model("retail_price.retail_price"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('retail_price.object', {
#             'object': obj
#         })
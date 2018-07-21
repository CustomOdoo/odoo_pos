# -*- coding: utf-8 -*-
from odoo import http

# class CustomProduct(http.Controller):
#     @http.route('/custom_product/custom_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_product/custom_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_product.listing', {
#             'root': '/custom_product/custom_product',
#             'objects': http.request.env['custom_product.custom_product'].search([]),
#         })

#     @http.route('/custom_product/custom_product/objects/<model("custom_product.custom_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_product.object', {
#             'object': obj
#         })
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

{
    'name': "Sale Order Multi Product Selection",
    'version': "11.0.0.1",
    'summary': "This module allows you to select Multiple product in sale order at a time on single click.",
    'category': 'Sale Management',
    'description': """
        This module allows you to select Multiple product in sale order on single click.
         sale order add multi product
         product add
         multiple product add in sale order quickly
         easy add product in sale order on single click
         create sale order from product
    """,
    'author': "Sitaram",
    'website': " ",
    'depends': ['base', 'sale_management', 'product'],
    'data': [
        'views/sale.xml',
        'views/product.xml'
    ],
    'demo': [],
    "license": "AGPL-3",
    'images': ['static/description/banner.png'],
    'live_test_url': 'https://youtu.be/0KFUawEdMpk',
    'installable': True,
    'application': True,
    'auto_install': False,
}

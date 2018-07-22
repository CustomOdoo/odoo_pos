# -*- coding: utf-8 -*-
{
    'name': "custom product",
    'version': '1.0',
    'sequence': 1,
    'category': 'Product',

    'summary': """
        Custom product""",

    'description': """
        Custom product with added fields
    """,

    'author': "SPH Consult",
    'website': "http://www.swahilipothub.co.ke",
    "support": "info@swahilipothub.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template.xml',
        # 'views/product_list.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
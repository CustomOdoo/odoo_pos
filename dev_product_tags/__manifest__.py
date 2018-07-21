# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Devintelle Software Solutions (<http://devintelle.com>).
#
##############################################################################

{
    'name': 'Product Tags',
    'version': '1.0',
    'sequence': 1,
    'category': 'Product',
    'description': """
        App will Add tags into product Screen
        
        Product Tags
    """,
    'summary': 'App will Add tags into product Screen',
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['product'],
    'data': [
        'security/tags_security.xml',
        'security/ir.model.access.csv',
        'views/product_template.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

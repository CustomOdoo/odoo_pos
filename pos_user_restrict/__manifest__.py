# -*- coding: utf-8 -*-
#############################################################
#
#    Garazd Creation, Ukraine
#    Copyright (C) 2018 Garazd Creation (<https://garazd.biz/>).
#    Author: Yurii Razumovskyi (<support@garazd.biz>)
#
#############################################################
{
    'name': 'Restriction of POS User',
    'version': '11.0.1.0.1',
    'category': 'Point of Sale',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'license': 'LGPL-3',
    'summary': """Limits the POS User to available Points of Sale.""",
    'description': 'Allow setting available Points of Sale for users. Restricts access for POS users to Points of Sales.',
    'images': ['static/description/banner.png'],
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/pos_user_restrict_security.xml',
        'views/res_users_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}

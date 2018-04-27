# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Amaroo Customization',
    'version' : '1.0',
    'summary': 'Get default account and tax from vendor',
    'sequence': 30,
    'description': """
Get default expense account and tax from vendor in invoice line
    """,
    'category': 'Custom',
    'website': 'https://www.broadtech-innovations.com',
    'images' : [],
    'depends' : ['account', 'purchase'],
    'data': [
        'views/account_invoice_view.xml',
        'views/partner_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

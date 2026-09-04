# -*- coding: utf-8 -*-
{
    'name': "Prevent Inventory Valuation Auto-Change",
    'summary': "Prevents automatic inventory valuation method from changing to manual during settings updates",
    'author': "Salai Thomas",
    'website': "https://github.com/Salai-Thomas",
    'category': 'Inventory/Inventory',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    'depends': [
        'stock_account',
    ],
    'data': [
        'views/res_config_setting_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# -*- coding: utf-8 -*-
{
    'name': "Restrict Sale Order Cancellation",

    'summary': "Prevents cancellation of Sale Orders if the related inventory is already validated.",

    'description': """
        Restrict Sale Order Cancellation
        =================================

        This module restricts users from cancelling a Sale Order once the corresponding inventory receipt (delivery order) has been validated. It helps maintain data integrity between sales and inventory processes.
    """,

    'author': "Salai Thomas",
    'website': "https://www.linkedin.com/in/salai-thomas-6a7201267",

    'category': 'Sales',
    'version': '15.0.1',

    'depends': ['base', 'sale', 'stock'],
    'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}

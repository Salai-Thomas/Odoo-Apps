{
    'name': "Purchase Create Bill",

    'summary': "Restores the Create Bill button on purchase orders for simplified invoicing.",

    'description': """
    This module reintroduces the 'Create Bill' button directly onto the Purchase Order form, 
    allowing users to quickly generate vendor bills from their purchases, mirroring 
    workflows from previous Odoo versions.
        """,

    'author': "Salai Thomas",
    'website': "https://www.linkedin.com/in/salai-thomas-6a7201267",
    'category': 'Purchases',
    'version': '19.0.1.0.0',

    'depends': ['purchase'],

    'data': [
        'views/purchase_order_form_view_inherit.xml'
    ],
    'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}


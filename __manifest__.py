# -*- coding: utf-8 -*-
{
    'name': "Personalizaciones - Intresco",

    'summary': """
        Personalizaciones para Intresco SAS""",

    'description': """
        Personalizaciones para Intresco SAS
    """,

    'author': "Intresco SAS",
    'website': "http://www.intresco.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_axis_helpdesk'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/helpdesk_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

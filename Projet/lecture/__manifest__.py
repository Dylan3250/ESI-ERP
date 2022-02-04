# -*- coding: utf-8 -*-
{
    'name': "Sales of books",

    'summary': """
        The goal of the project is to develop a book sales module
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Jeremie SHESHIE (54627) & Dylan BRICAR (54027)",
    'website': "http://www.he2b.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/book_menu.xml',
        'views/book_view.xml',
        'views/product_template_view.xml',
        'views/res_partnair_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # Edited by ESI
    'application': True,
}

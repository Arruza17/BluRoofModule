# -*- coding: utf-8 -*-
{
    'name': "BluRoof application",

    'summary': """
       Application to make CRUD operations with Dwellings, Users and all the possible options between them""",

    'description': """
        Application used to create information about Dwellings and Users. The last ones will be able to comment on dwellings. 
    """,

    'author': "BluRoof",
    'website': "https://github.com/Arruza17/BluRoofModule",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Real State',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/users_view.xml',
        'reports/bluroof_report_guest_test.xml',
   ],
   
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
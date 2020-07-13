# -*- coding: utf-8 -*-
{
    'name': "App Fields",

    'summary': """
        Extend a bunch of models""",

    'description': """
        Long description of module's purpose
    """,

    'author': "eric@sailotech",
    'website': "http://www.yourcompany.com",

    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],

}

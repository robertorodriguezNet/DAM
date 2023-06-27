# -*- coding: utf-8 -*-
{
    'name': "agenda",

    'summary': """
        Módulo que gestiona los teléfonos de los contactos""",

    'description': """
        Módulo de pruebas para gestionar una agenda telefónica
    """,

    'author': "Roberto Rodríguez",
    'website': "http://www.robertorodriguez.net",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/agenda_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

        #Indicar que es una aplicación
    'application': True,

    #Especificamos la licencia
    'license': 'LGPL-3',

}

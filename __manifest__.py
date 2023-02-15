# -*- coding: utf-8 -*-
{
    'name': "background-color change",
    'summary': """
        Odoo 16 background-color change in Helpdesk module""",
    'description': """
        Odoo 16 background-color change in Helpdesk module
    """,
    'author': "Sidean",
    'website': "https://www.sidean.com",
    'category': 'Customizations',
    'version': '0.1',
    'depends': ['mail', 'helpdesk'],
    # always loaded
    'data': [
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}

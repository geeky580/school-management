# -*- coding: utf-8 -*-
{
    'name' : 'Test_Module',
    'version' : '1.0',
    'summary': 'We are just trying to install first module',
    'sequence': -10,
    'description': """""",
    'category': 'Marketing',
    'website': 'https://www.odoomates.tech/',
    'license': 'LGPL-3',
    'depends' : ['hr' ],
    'data': [
        'View/student.xml',
        'Security/ir.model.access.csv',
        'View/classm.xml',
        'View/fees.xml',
        'View/subject.xml',
        'Security/security.xml',
        'View/teacher.xml',
        "wizards/create_exam.xml",
        'report/report.xml',
        'report/student_card.xml'
    ],
    'demo': [ ],
    'qweb': [ ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

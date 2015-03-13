# -*- coding: utf-8 -*-
{
    'name': 'Display Product Quantity',
    'version': '1.0',
    'category': 'Products',
    'description': """
        Dispaly BOM product quantity at Sales.
    """,
    'author': 'Simon',
    'website': 'www.github.com',
    'depends': ["stock",'mrp'],
    'init_xml': [],
    'data': [
        "product_view.xml",
        #"mail_data.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'installable': True,
    'auto_install': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
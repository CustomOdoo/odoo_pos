{
    'name': 'Combo Product',
    'category': 'Product',
    'author': 'SPH Consult',
    'website': "http://www.swahilipothub.co.ke",
    "support": "info@swahilipothub.co.ke",
    'version': '1.0',
    'description':
        """
Combo Product.
========================
Create Combo Product like (CPU + Processor + Mouse + Keyboard) is in Producr Computer .

        """,
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/combo_product_view.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
}

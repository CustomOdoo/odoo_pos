{
    'name': 'Combo Product',
    'category': 'Product',
    'author': 'TechnoSquare',
    'website': "http://www.technosquare.in",
    "support": "info@technosquare.in",
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

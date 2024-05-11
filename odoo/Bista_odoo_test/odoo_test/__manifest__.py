{
    "name": "Bista Odoo Test",
    "version": "0.1",
    "website": "https://www.mahesh.com",
    "author": "Mahesh",
    "description": """
        Long description of module's purpose
    """,
    "category": "Bussines",
    "depends": ["product", "sale", "purchase", "base"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/wizard_form.xml",
        "views/product.xml",
        "views/inherit_view.xml",
        "views/business_sale.xml",
        "views/product_master.xml",
        "views/product_tag_views.xml",
        "views/config_view.xml",
        "views/sale_order_view.xml",
        "views/menu.xml"
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

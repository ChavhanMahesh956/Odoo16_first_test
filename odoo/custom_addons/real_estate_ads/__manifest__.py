{
    "name": "Real Estate Ads",
    "version": "0.1",
    "website": "https://www.odooguys.com",
    "author": "Mahesh",
    "description": """
        Long description of module's purpose
    """,
    "category": 'Sales',
    "depends": ['base'],
    "data": [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/menu_items.xml',  
        'data/property_type.xml',
        # 'data/estate.property.type.csv',
    ],
    "demo": [
        'demo/property_tag.xml'
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}


from odoo import api, fields, models

class BusinessSale(models.Model):
    _name = "product.sale"
    _description = "Product Business Sale"
    
    name = fields.Char(string="Name", required=True)
    
    

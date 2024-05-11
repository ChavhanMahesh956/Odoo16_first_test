from odoo import api, fields, models

class Property(models.Model):
    _name = "branch.product.data"
    _description = "Product Master"
    
    name = fields.Char(string="Name", required=True)
    cost = fields.Float(string="Cost")
    sales_price = fields.Float(string="Sales_price")
    product = fields.Many2many('product.template',string="Product")
    
    
    
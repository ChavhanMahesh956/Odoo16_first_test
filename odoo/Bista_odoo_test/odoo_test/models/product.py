from odoo import api, fields, models
# from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = "product.style"
    _description = "Product Style"
    
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True) 
    
    sql_constraints = [
        ('code_unique', 'unique(code)', 'The code must be unique!'),
    ]

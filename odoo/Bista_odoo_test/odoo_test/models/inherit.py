from odoo import api, fields, models, tools

class ProductConfig(models.Model):
    _inherit = ['product.template']
    
    name_inherit= fields.Many2one('product.style',string="Product Style")
    
    Done_business  = fields.Many2many('product.sale')
    tag = fields.Many2many('product.tags',string="Tags")
    

class ProductExtendLine(models.Model):
    _inherit = ['sale.order.line']
    
    user1= fields.Many2one('product.style') 
    
    @api.onchange('product_template_id')    
    def _onchange_product_template_id(self):
        if self.product_template_id:
            self.user1 = self.product_template_id.name_inherit.id
        else:
            self.user1 = False
        
class ProductCustomer(models.Model):
    _inherit = ['res.partner']
    
    customer_rating = fields.Selection([
        ('one_star','One_Star'),
        ('two_star','Two_Star'),
        ('three_star','Three_Star'),
        ('four_star','Four_Star'),
        ('five star','Five Star')],
        string="Customer Rating") 
    
        
class ProductSales(models.Model):
    _inherit = ['sale.order']
      
    customer_rating1 = fields.Selection([('one_star','One_Star'),('two_star','Two_Star'), ('three_star','Three_Star'),('four_star','Four_Star'),('five star','Five Star')], string="Customer Rating")
    
    


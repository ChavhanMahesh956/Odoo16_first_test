from odoo import api, models, fields
    
class Wizard(models.TransientModel):
    _name = 'wizard'
    _description = "Add Wizard to the Sale Order"

    product_id = fields.Many2one('product.template', string='Product')
    quantity = fields.Float(string='Quantity')
    
    
    def wizard_action(self):
        self.ensure_one()
        sale_order = self.env['sale.order'].browse(self.env.context.get('active_ids'))
        sale_order_line_vals = {
                'product_id': self.product_id.id,
                'product_uom_qty': self.quantity,
            }
        sale_order.update({
            'order_line':[(0,0,sale_order_line_vals)]
        })
        return True
        
    

class SaleOrderinherit(models.Model):
    _inherit = 'product.template'
    
    wizard_ids = fields.One2many('wizard', 'product_id', string='Wizards Product')



    
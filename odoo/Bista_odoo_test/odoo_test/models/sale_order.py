from odoo import api, fields, models, tools
        
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    purchase_order = fields.Many2one('purchase.order', string="Purchase Order", store=True, readonly=True)

    
    def custom_button_action(self):
        purchase_order_lines = []
        for sale in self:
            for line in sale.order_line:
                purchase_order_line_data = {
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'product_qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                    'order_id': sale.id,
                    'company_id': sale.company_id.id,
                    'partner_id': sale.partner_id.id
                }
            purchase_order_lines.append((0, 0, purchase_order_line_data))
            
            purchase_data = {
                'partner_id':self.partner_id.id,
                'company_id':self.company_id.id,
                'order_line':purchase_order_lines,
            }
        
        purchase_order = self.env['purchase.order'].create(purchase_data)
        sale.purchase_order = purchase_order.id
        return True
        

    # def prepare_order_line(self):
    #     order_line_vals = []
    #     for line in self.order_line:
    #         order_line_vals.append({
    #             'name': line.name,
    #             'product_id': line.product_id.id,
    #             'product_qty': line.product_uom_qty,
    #             'order_id': self.id, 
    #             'price_unit': line.price_unit,
    #         })
    #     return order_line_vals
    
    # def custom_button_action(self):
    #     order_line_vals = self.prepare_order_line()
    #     print("order_line_vals", order_line_vals)
    #     new_purchase_order = self.env['purchase.order'].create({
    #         'partner_id': self.partner_id.id,
    #         'order_line': [(0, 0, vals) for vals in order_line_vals], 
    #         'date_order': self.date_order,
    #     })
        
    #     self.purchase_order = new_purchase_order.id
    #     return True

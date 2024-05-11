from datetime import timedelta
from odoo import api, fields, models

class DateTimeChange(models.Model):
    _inherit = 'sale.order'
    _description = "Change The DateTime"
    
    new_Quotation_Date = fields.Datetime(string="New Quotation Date")

    @api.onchange('date_order')
    def onchange_field_datetime(self):
        if self.date_order:
            original_datetime = fields.Datetime.from_string(self.date_order)

            new_datetime = original_datetime

            for i in range(5): 
                new_datetime += timedelta(days=1)
                while new_datetime.weekday() >= 5:  
                    new_datetime += timedelta(days=1)

            self.new_Quotation_Date = new_datetime.strftime('%Y-%m-%d %H:%M:%S')
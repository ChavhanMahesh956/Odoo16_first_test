from odoo import api, fields, models

class ConfigTags(models.Model):
    _name = "config.tags"
    _description = "Config Tags"
    
    
    name = fields.Char(string="Name", required=True)
    color = fields.Char(string="Color")
    

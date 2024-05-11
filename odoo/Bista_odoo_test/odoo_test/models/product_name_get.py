
from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    
    def name_get(self):
        res = super(ProductProduct, self).name_get()
        result = []
        for product_id, name in res:
            product = self.browse(product_id)
            if product.categ_id:
                name = '%s (%s)' % (name, product.categ_id.name)
            result.append((product_id, name))
        return result
    
    
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:
            category_ids = self.env['product.category'].search([('name', operator, name)])
            if category_ids:
                product_ids = self.search([('categ_id', 'in', category_ids.ids)]).ids
                args += [('id', 'in', product_ids)]
                name = ''
        return super(ProductProduct, self)._name_search(name=name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)
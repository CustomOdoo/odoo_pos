from odoo import models, fields


class PromotionProduct(models.Model):
    _inherit = 'product.template'

    is_promotion_product = fields.Boolean(string="Promotion Product", default=False,help='This is a promotion product')

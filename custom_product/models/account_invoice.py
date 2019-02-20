from odoo import models, fields, api, _ 


class AcountInvoice(models.Model):
	_inherit = 'account.invoice'

	packing_size = fields.Char(related='invoice_line_id.product_id.packing_size')
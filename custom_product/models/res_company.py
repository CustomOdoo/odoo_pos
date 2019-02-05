from odoo import models, fields, api, _
    

class ResPartner(models.Model):    
    _inherit = 'res.company'

    vat = fields.Char('TRN')
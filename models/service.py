# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models

class service(models.Model):
    _name = 'bluroof.service'

    serviceType = fields.Selection(["HEALTH", "RESTORATION", "TRANSPORT", "EDUCATION", "TRAVELLING", "SHOPPING"], String="Service type")
    address = fields.Char()
    name = fields.Char()
    neighbourhood_id = fields.Many2one('bluroof.neighbourhood', ondelete='cascade', string="Neighbourhood")
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
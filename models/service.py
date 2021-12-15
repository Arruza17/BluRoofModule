# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class service(models.Model):
        _name = 'bluroof.service'

        type = fields.Selection()
        address = fields.Char()
        name = fields.Char()
        neighbourhood_id = fields.Many2one('bluroof.neighbourhood',ondelete='cascade', string="Neighbourhood")
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
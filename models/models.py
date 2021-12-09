# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class bluroof(models.Model):
        _name = 'bluroof.bluroof'

        name = fields.Char()
        value = fields.Integer()
        value2 = fields.Float()
        description = fields.Text()
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
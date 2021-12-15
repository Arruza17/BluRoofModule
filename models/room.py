# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class bluroof(models.Model):
        _name = 'bluroof.room'
        _inherit='bluroof.dwelling'
        naturalLight = fields.Boolean()
        nOutlets = fields.Integer()
        description = fields.Text()
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

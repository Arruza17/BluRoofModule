# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class neighbourhood(models.Model):
        _name = 'bluroof.neighbourhood'
      
        name = fields.Char()
        postCode = fields.Integer()
        dwellings_id = fields.One2many('bluroof.dwelling','neighbourhood_id',ondelete='cascade', string="Dwellings")
        services_id = fields.One2many('bluroof.service','neighbourhood_id', ondelete='cascade', string="Services")
        
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
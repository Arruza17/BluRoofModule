# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class Dwelling(models.Model):
        _name = 'bluroof.dwelling'

        address = fields.String()
        hasWiFi = fields.Boolean()
        squareMeters = fields.Double()
        neighbourhood_id = fields.Many2one('bluroof.neighbourhood',
        ondelete = 'cascade', String = "Neighbourhood", index = True)
        constructionDate = fields.Date()
        host_id = fields.Many2one('bluroof.owner',
        ondelete = 'cascade', String = "Host", index = True)
        rating = fields.Float()
        comments = fields.One2many('bluroof.comment','comments',
        ondelete = 'cascade', String = "Comments", index = True)
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
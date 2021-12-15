# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class Comment(models.Model):
        _name = 'bluroof.coment'

        text = fields.String()
        rating = fields.Short()
        commentDate = fields.DateTime()
        commenter_id = fields.Many2one('bluroof.guest',
        ondelete = 'cascade', String = "Commenter", index = True)
        dwelling_id = fields.Many2one('bluroof.dwelling',
        ondelete = 'cascade', String = "Dwelling", index = True)
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
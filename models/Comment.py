# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models

class Comment(models.Model):
    _name = 'bluroof.comment'
    text = fields.Text()
    rating = fields.Integer()
    commentDate = fields.Datetime()
    commenter_id = fields.Many2one('bluroof.guest',
                                   ondelete='cascade', String="Commenter", index=True)
    dwelling_id = fields.Many2one('bluroof.dwelling',
                                  ondelete='cascade', String="Dwelling", index=True)
        
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
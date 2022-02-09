# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models

class comment(models.Model):
    _name = 'bluroof.comment'
    text = fields.Text()
    rating = fields.Integer()
    commentDate = fields.Datetime()
    commenter_id = fields.Many2one('res.users', ondelete='cascade', String="Commenter")
    dwelling_id = fields.Many2one('bluroof.dwelling', ondelete='cascade', String="Dwelling")
        
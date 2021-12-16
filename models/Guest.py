# -*- coding: utf-8 -*-
from odoo import api, fields, models

class User (models.Model):
    __name = 'bluroof.guest'
    __inheritance = 'bluroof.user'
    
    actualState = fields.Selection(["WORKER","STUDENT","BOTH","UNEMPLOYED"],String="Actual state")
    comments=  fields.One2many('bluroof.dwelling', 'commenter_id', string="Comments")
    
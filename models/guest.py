# -*- coding: utf-8 -*-
from odoo import api, fields, models

class guest (models.Model):
    _name = 'bluroof.guest'
    _inherit =  'res.users'
    
    actualState = fields.Selection(["WORKER","STUDENT","BOTH","UNEMPLOYED"],String="Actual state")
    comments=  fields.One2many('bluroof.dwelling', 'commenter_id', string="Comments")
    
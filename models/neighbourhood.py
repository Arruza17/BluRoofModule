# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError


class neighbourhood(models.Model):
    _name = 'bluroof.neighbourhood'   
    name = fields.Char(required='true')
    postCode = fields.Integer()
    dwellings = fields.One2many('bluroof.dwelling', 'neighbourhood_id', ondelete='cascade', string="Dwellings")
    services = fields.One2many('bluroof.service', 'neighbourhood_id', ondelete='cascade', string="Services") 
    
    @api.constrains('postCode')
    def _check_postCode(self):
        for neighbourhood in self:
            if neighbourhood.postCode > 5:
                raise ValidationError("Post code cannot be higher than 5 digits")
    
    @api.constrains('name')
    def _check_name(self):
        for neighbourhood in self:
            if neighbourhood.name.isnumeric():
                raise ValidationError("Name field cannot contain numbers")
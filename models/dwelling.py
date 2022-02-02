# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions
import datetime

class dwelling(models.Model):
    _name = 'bluroof.dwelling'
    address = fields.Char(String="Address",required=True)
    hasWiFi = fields.Boolean() 
    squareMeters = fields.Float()
    neighbourhood_id = fields.Many2one('bluroof.neighbourhood', ondelete='cascade', String="Neighbourhood", index=True)
    constructionDate = fields.Date()  
    rating = fields.Float()
    host_id = fields.Many2one('bluroof.owner', ondelete='cascade', String="Host", index=True)
    comments = fields.One2many('bluroof.comment', 'dwelling_id', ondelete='cascade', String="Comments", index=True)
    
    @api.constrains('squareMeters')
    def _verify_valid_squareMeters(self):
        if self.squareMeters <= 0:
            raise exceptions.ValidationError("The squareMeters must greater than 0, try again")

    @api.constrains('constructionDate')
    def _verify_valid_constructionDate(self):
        strConsDate = datetime.datetime.strptime(self.constructionDate, '%Y-%m-%d')
        if strConsDate >= datetime.datetime.now():
            raise exceptions.ValidationError('Expiration date must be after today.')
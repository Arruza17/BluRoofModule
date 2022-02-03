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
         
    @api.onchange('squareMeters')
    def _verify_valid_squareMeters(self):
        if self.squareMeters <= 0:
            return {
                'warning': {
                'title': "'squareMeters' value information",
                'message': "The squareMeters must greater than 0",
                },
            }

    @api.constrains('constructionDate')
    def _verify_valid_constructionDate(self):
        for dwelling in self:
            strConsDate = datetime.datetime.strptime(self.constructionDate, '%Y-%m-%d')
            if strConsDate >= datetime.datetime.now():
                raise exceptions.ValidationError('Construction date must be at least before today.')

    @api.constrains('rating')
    def _verify_valid_rating0(self):
        for dwelling in self:
            if dwelling.rating <= 0:
                raise exceptions.ValidationError("The rating must be greater than 0, try again")

    @api.constrains('rating')
    def _verify_valid_rating5(self):
        for dwelling in self:
            if dwelling.rating > 5:
                raise exceptions.ValidationError("The rating must be lower than 5, try again")
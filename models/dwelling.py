# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models

class dwelling(models.Model):
    _name = 'bluroof.dwelling'
    address = fields.Char(String="Address")
    hasWiFi = fields.Boolean() 
    squareMeters = fields.Float()
    neighbourhood_id = fields.Many2one('bluroof.neighbourhood', ondelete='cascade', String="Neighbourhood", index=True)
    constructionDate = fields.Date()  
    rating = fields.Float()
    host_id = fields.Many2one('bluroof.owner', ondelete='cascade', String="Host", index=True)
    comments = fields.One2many('bluroof.comment', 'dwelling_id', ondelete='cascade', String="Comments", index=True)
        
    @api.onchange('address', 'attendee_ids')
    def _verify_null_values(self):
        if self.address:
            return {
                'warning': {
                    'title': "Empty value",
                    'message': "The number of available seats may not be negative",
                    },
                }


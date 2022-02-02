# -*- coding: utf-8 -*-
#enum = selection
#first commit
from asyncio.windows_events import NULL
from odoo import api
from odoo import fields
from odoo import models

class service(models.Model):
    _name = 'bluroof.service'

    SERVICES = [
        ('0', 'HEALTH'),
        ('1', 'RESTORATION'),
        ('2', 'TRANSPORT'),
        ('3', 'EDUCATION'),
        ('4', 'TRAVELLING'),
        ('5', 'SHOPPING')    
        ]

    serviceType = fields.Selection(SERVICES, String="Service type")
    address = fields.Char()
    name = fields.Char()
    neighbourhood_id = fields.Many2one('bluroof.neighbourhood', ondelete='cascade', string="Neighbourhood")
        
 @api.onchange('address')
    def _check_empty_address(self):
        if self.address==NULL:
            return{
               'warning': {'title': "No address",'message': "Your must imput the service address",},
            }

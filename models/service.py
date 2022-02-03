# -*- coding: utf-8 -*-
#enum = selection
#first commit


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

    serviceType = fields.Selection(SERVICES, String="Service type", required='true')
    address = fields.Char()
    name = fields.Char()
    neighbourhood_id = fields.Many2one('bluroof.neighbourhood', ondelete='cascade', string="Neighbourhood")

    @api.onchange('serviceType')
    def on_change_serviceTypeNull(self):
        if(not(self.serviceType)):
            return{
            'warning':{
            'title':'null service type',
            'message':'Service type combo box is empty. Please select a value'
            }
        }
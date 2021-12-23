# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models

class facility(models.Model):
    _name = 'bluroof.facility'
    FACILITIES = [
        ('0', 'WASHING_MACHINE'),
        ('1', 'DRYING_MACHINE'),
        ('2', 'FRIDGE'),
        ('3', 'WARDROBE'),
        ('4', 'FURNACE')
    ]
    
    facilityType = fields.Selection(FACILITIES , String="Facility Type")
    adquisitionDate = fields.Date()       
    description = fields.Text()
   
    #flatFacilities = fields.One2many('bluroof.flatfacility', 'facility_id', ondelete='cascade', string="Flat Facilities")
    
    
   
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
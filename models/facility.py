# -*- coding: utf-8 -*-
#enum = selection
#first commit
import datetime
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError
class facility(models.Model):
    _name = 'bluroof.facility'

    FACILITIES = [
        ('0', 'WASHING_MACHINE'),
        ('1', 'DRYING_MACHINE'),
        ('2', 'FRIDGE'),
        ('3', 'WARDROBE'),
        ('4', 'FURNACE')
    ]
    
    facilityType = fields.Selection(FACILITIES, String="Facility Type")
    adquisitionDate = fields.Date()       
    description = fields.Text()
   
    flatFacilities = fields.One2many('bluroof.flatfacility', 'facility_id', ondelete='cascade', string="Flat Facilities")
    @api.constrains('adquisitionDate')
    def _check_dateNotNull(self):
        for record in self:
            if (not (record.date and record.date.strip())):
                raise ValidationError("The date cant be null")

    

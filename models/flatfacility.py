# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class bluroof(models.Model):
        _name = 'bluroof.flatfacility'
        flat_id=fields.Many2One('bluroof.flat',ondelete='cascade',string="Flat",required=true)
        facility_id= fields.Many2One('bluroof.facility',ondelete='cascade',string="Facility",required=true)
        facility_condition=fields.Selection()
        description = fields.Text()
        

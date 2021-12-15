# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class facility(models.Model):
        _name = 'bluroof.facility'

        type = fields.Selection()
        adquisitionDate = fields.Date       
        description = fields.Text()
        flatFacilities_id = fields.One2many('bluroof.flatfacilities','facility_id', ondelete='cascade', string="Flat Facilities")
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models

class flatfacility(models.Model):
    _name = 'bluroof.flatfacility'
    flat_id = fields.Many2one('bluroof.flat', ondelete='cascade', String="Flat")
    facility_id = fields.Many2one('bluroof.facility', ondelete='cascade', String="Facility")
    facility_condition = fields.Selection(["NEW", "BROKEN", "WORKING"], String="Facility condition")
    description = fields.Text()
        

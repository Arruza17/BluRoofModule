# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class Flat(models.Model):
        _name = 'bluroof.flat'
        _inherit= 'bluroof.dwelling'
        nRooms = fields.Integer()
        nBathrooms = fields.Integer()
        description = fields.Text()
        flatfacility_id=fields.One2Many('bluroof.flatfacility',ondelete='cascade',string="Flat facilities",required=true)

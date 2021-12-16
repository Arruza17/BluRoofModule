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
        flatFacilities =fields.One2many('bluroof.flatfacility','flat_id',string="Flat facilities")

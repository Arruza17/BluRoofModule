# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class flat(models.Model):
        _name = 'bluroof.flat'
        _inherit= 'bluroof.dwelling'

        nRooms = fields.Integer()
        nBathrooms = fields.Integer()
        description = fields.Text()
        flatFacilities =fields.One2many('bluroof.flatfacility','flat_id',string="Flat facilities")

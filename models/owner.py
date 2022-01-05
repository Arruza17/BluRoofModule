# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class owner (models.Model):
    _inherit = 'bluroof.user'
    _name = 'bluroof.owner'

    isResident = fields.Boolean(string="Is resident")
    dwellings = fields.One2many('bluroof.dwelling', 'host_id', string="Dwellings")
# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class User (models.Model):
    __name = 'bluroof.owner'
    __inheritance = 'bluroof.user'
    isResident = fields.Boolean(string="Is resident")
    dwellings = fields.One2many('bluroof.dwelling', 'host_id', string="Dwellings")
# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import models, fields, api

class room(models.Model):
        _name = 'bluroof.room'
        _inherit='bluroof.dwelling'
        naturalLight = fields.Boolean()
        nOutlets = fields.Integer()
        description = fields.Text()
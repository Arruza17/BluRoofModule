# -*- coding: utf-8 -*-
#enum = selection
#first commit
from odoo import api
from odoo import fields
from odoo import models

class room(models.Model):
    _name = 'bluroof.room'
    _inherit = 'bluroof.dwelling'
    naturalLight = fields.Boolean(default="True")
    nOutlets = fields.Integer()
    description = fields.Char()
# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

class guest (models.Model):
    _inherit = 'bluroof.user'
    _name = 'bluroof.guest'

    ACTUAL_STATE = [
        ('0', 'WORKER'),
        ('1', 'STUDENT'),
        ('2', 'BOTH'),
        ('3', 'UNEMPLOYED')
    ]

    actualState = fields.Selection(ACTUAL_STATE, String="Actual state")
    comments = fields.One2many('bluroof.comment', 'commenter_id', string="Comments")
    
    @api.constrains('actualState')
    def _check_actual_state_not_null(self):
            if (not (self.actualState and self.actualState.strip())):
                raise exceptions.ValidationError("You must input the type of actual state")
     
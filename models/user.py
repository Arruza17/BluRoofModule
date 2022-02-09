# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

class user (models.Model):
    _inherit = 'res.users'

    birthDate = fields.Date(string="Date of birth")
    
    STATUS = [
        ('0', 'ENABLED'),  
        ('1', 'DISABLED')
        ]
 
    PRIVILEGE = [
        ('0', 'ADMIN'),
        ('1', 'HOST'),
        ('2', 'GUEST'),
        ]

    ACTUAL_STATE = [
        ('0', 'WORKER'),
        ('1', 'STUDENT'),
        ('2', 'BOTH'),
        ('3', 'UNEMPLOYED')
    ]
    
    userStatus = fields.Selection(STATUS, string="Status")
    userPrivilege = fields. Selection(PRIVILEGE, string="Privilege")
    lastPasswordChange = fields.Datetime(string="Last password change")
    phoneNumber = fields.Char(string="Telephone number")

    #Guest
    actualState = fields.Selection(ACTUAL_STATE, String="Actual state")
    comments = fields.One2many('bluroof.comment', 'commenter_id', string="Comments")
    
    #Host
    isResident = fields.Boolean(string="Is resident")
    dwellings = fields.One2many('bluroof.dwelling', 'host_id', string="Dwellings")
    
    @api.constrains('actualState')
    def _check_actual_state_not_null(self):
            if (not (self.actualState and self.actualState.strip())):
                raise exceptions.ValidationError("You must input the type of actual state")


    @api.onchange('phoneNumber')
    def _verify_valid_number(self):
        if not len(str(self.phoneNumber)) == 9 :
            return {
                'warning': {
                'title': "iNFORMATION:",
                'message': "The phone number must contain 9 characters",
            },
        }


    
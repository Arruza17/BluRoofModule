# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class user (models.Model):
    _inherit = 'res.users'
    _name = 'bluroof.user'

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


    status = fields.Selection(STATUS, string="Status")
    privilege = fields. Selection(PRIVILEGE, string="Privilege")
    lastPasswordChange = fields.Datetime(string="Last password change")
    phoneNumber = fields.Char(string="Telephone number")



    
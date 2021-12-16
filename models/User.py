# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class User (models.Model):
    __name = 'bluroof.user'
    __inheritance = 'res.user'
    birthDate = fields.Date(string="Date of birth")
    status = fields.Selection(["WORKER", "STUDENT", "BOTH", "UNEMPLOYED"], string="Status")
    privilege = fields. Selection(["ADMIN", "HOST", "GUEST"], string="Privilege")
    lastPasswordChange = fields.Datetime(string="Last password change")
    phoneNumber = fields.Char(string="Telephone number")
    lastSignIns = fields.One2many('bluroof.lastSignIn', 'user_id', string="Last sign ins")
    
    
    
    
    
    
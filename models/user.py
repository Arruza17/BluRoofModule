# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class user (models.Model):
    _inherit = 'res.users'
    birthDate = fields.Date(string="Date of birth")
    status = fields.Selection(["WORKER", "STUDENT", "BOTH", "UNEMPLOYED"], string="Status")
    privilege = fields. Selection(["ADMIN", "HOST", "GUEST"], string="Privilege")
    lastPasswordChange = fields.Datetime(string="Last password change")
    phoneNumber = fields.Char(string="Telephone number")

   

    
    
    
    
    
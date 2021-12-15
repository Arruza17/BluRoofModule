from odoo import models, fields, api

class User (models.Model):
    __name = 'bluroof.user'
    __inheritance = 'res.user'
    birthDate = fields.Date(string="Date of birth")
    status = fields.Selection(string ="Status")
    privilege = fields. Selection(string= "Privilege")
    lastPasswordChange= fields.Datetime(string="Last password change")
    phoneNumber = fields.Char(string="Telephone number")
    lastSignIns = fields.One2many('bluroof.lastSignIn', 'user_id', string="Last sign ins")
    
    
    
    
    
    
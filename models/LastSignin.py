from odoo import models, fields, api

class User (models.Model):
    __name = 'bluroof.lastSignIn'

    lastSignIn = fields.Datetime(string="Last sign in change")
    user_id = fields.Many2one('bluroof.user',ondelete='cascade', string="User")

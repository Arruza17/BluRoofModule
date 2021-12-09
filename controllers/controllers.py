# -*- coding: utf-8 -*-
from odoo import http

# class Bluroof(http.Controller):
#     @http.route('/bluroof/bluroof/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bluroof/bluroof/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bluroof.listing', {
#             'root': '/bluroof/bluroof',
#             'objects': http.request.env['bluroof.bluroof'].search([]),
#         })

#     @http.route('/bluroof/bluroof/objects/<model("bluroof.bluroof"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bluroof.object', {
#             'object': obj
#         })
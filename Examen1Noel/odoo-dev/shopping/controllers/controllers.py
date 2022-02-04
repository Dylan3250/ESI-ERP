# -*- coding: utf-8 -*-
# from odoo import http


# class Shopping(http.Controller):
#     @http.route('/shopping/shopping/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shopping/shopping/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shopping.listing', {
#             'root': '/shopping/shopping',
#             'objects': http.request.env['shopping.shopping'].search([]),
#         })

#     @http.route('/shopping/shopping/objects/<model("shopping.shopping"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shopping.object', {
#             'object': obj
#         })

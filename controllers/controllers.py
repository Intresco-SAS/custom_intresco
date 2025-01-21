# -*- coding: utf-8 -*-
# from odoo import http


# class Custom-addons/customIntresco(http.Controller):
#     @http.route('/custom-addons/custom_intresco/custom-addons/custom_intresco', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/custom_intresco/custom-addons/custom_intresco/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/custom_intresco.listing', {
#             'root': '/custom-addons/custom_intresco/custom-addons/custom_intresco',
#             'objects': http.request.env['custom-addons/custom_intresco.custom-addons/custom_intresco'].search([]),
#         })

#     @http.route('/custom-addons/custom_intresco/custom-addons/custom_intresco/objects/<model("custom-addons/custom_intresco.custom-addons/custom_intresco"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/custom_intresco.object', {
#             'object': obj
#         })

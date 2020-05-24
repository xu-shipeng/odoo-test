# -*- coding: utf-8 -*-
from odoo import http

# class XspTest(http.Controller):
#     @http.route('/xsp_test/xsp_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xsp_test/xsp_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xsp_test.listing', {
#             'root': '/xsp_test/xsp_test',
#             'objects': http.request.env['xsp_test.xsp_test'].search([]),
#         })

#     @http.route('/xsp_test/xsp_test/objects/<model("xsp_test.xsp_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xsp_test.object', {
#             'object': obj
#         })
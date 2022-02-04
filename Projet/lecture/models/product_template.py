from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    books_collection = fields.Many2many('lecture.book', string="Collection books", required=True)

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    book_ids = fields.Many2many('lecture.book', string='Book')
    book_count = fields.Integer('Book Count', compute='_compute_book_count', store=True)

    @api.depends("book_ids")
    def _compute_book_count(self):
        for partner in self:
            partner.book_count = len(partner.book_ids)

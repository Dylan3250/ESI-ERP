from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime


class Book(models.Model):
    _name = 'lecture.book'
    _description = 'Book Management'

    # Fields
    name = fields.Char('Name', help="What book is this ?", required=True)
    description = fields.Html('Description')
    picture = fields.Binary('Image')
    date = fields.Date('Date', default=datetime.today())
    nbPage = fields.Integer('Page number')
    author_ids = fields.Many2many('res.partner', string='Authors', default=lambda self: self.env.user)

    # Likes
    users_liked = fields.Many2many('res.users', string="Users who liked")
    current_user_liked = fields.Boolean(string="The current user likes this book ?", compute="_compute_user_liked")
    like_number = fields.Integer('Number of likes', compute='_compute_like_number')

    # Constraints
    _sql_constraints = [
        ('uniqueName', 'unique(name)', 'The book must be unique.'),
    ]

    @api.constrains('nbPage')
    def _check_nb_page(self):
        for book in self:
            if book.nbPage <= 0:
                raise ValidationError('Number of pages must be greater than 0')

    @api.constrains('date')
    def _check_date(self):
        for book in self:
            if book.date > date.today():
                raise ValidationError('Date must be earlier than today')

    # Likes
    def _compute_user_liked(self):
        self.current_user_liked = self.env.uid in self.users_liked.ids

    def like_book(self):
        if self.env.uid in self.users_liked.ids:
            self.write({
                'users_liked': [(3, self.env.uid)]  # remove on the list
            })
        else:
            self.write({
                'users_liked': [(4, self.env.uid)]  # add on the list
            })

    def _compute_like_number(self):
        for book in self:
            book.like_number = len(book.users_liked)

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
import psycopg2
import datetime


class TestBook(TransactionCase):
    def test_createBook(self):
        book = self.env['lecture.book'].create({
            'name': 'Book',
            'description': 'Description',
            'nbPage': '87',
            'date': datetime.date(2019, 1, 1),
        })

        self.assertEqual(book.name, 'Book')
        self.assertEqual(book.description, '<p>Description</p>')
        self.assertEqual(book.date, datetime.date(2019, 1, 1))
        self.assertEqual(book.nbPage, 87)

    def test_dateFuture(self):
        with self.assertRaises(ValidationError):
            self.env['lecture.book'].create({
                'name': 'BookNoExistSecond',
                'description': 'Description',
                'nbPage': '0',
                'date': datetime.date(9999, 1, 1),
            })

    def test_nbPageZero(self):
        with self.assertRaises(ValidationError):
            self.env['lecture.book'].create({
                'name': 'BookNoExistSecond',
                'description': 'Description',
                'nbPage': '0',
                'date': datetime.date(2019, 1, 1),
            })

    def test_nbPageNegative(self):
        with self.assertRaises(ValidationError):
            self.env['lecture.book'].create({
                'name': 'BookNoExist',
                'description': 'Description',
                'nbPage': '-1',
                'date': datetime.date(2019, 1, 1),
            })

    def test_checkUnique(self):
        self.env['lecture.book'].create({
            'name': 'BookUnique',
            'description': 'Description',
            'nbPage': '87',
            'date': datetime.date(2019, 1, 1),
        })

        with self.assertRaises(psycopg2.IntegrityError):
            self.env['lecture.book'].create({
                'name': 'BookUnique',
                'description': 'Description',
                'nbPage': '87',
                'date': datetime.date(2019, 1, 1),
            })

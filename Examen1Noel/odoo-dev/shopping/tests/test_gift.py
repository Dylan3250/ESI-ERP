from odoo.tests.common import TransactionCase


class TestGift(TransactionCase):

    def test_create(self):
        Gift = self.env['gift']
        with self.assertRaises(Exception):
            Gift.create({'name': 'Test Gift', 'price': -1.0, 'bought': False, 'task_id': None})

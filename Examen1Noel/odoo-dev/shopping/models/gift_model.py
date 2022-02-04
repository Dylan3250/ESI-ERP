from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)


class Gift(models.Model):
    _name = 'gift'

    name = fields.Char('Name', help="Nom du cadeau", required=True)
    price = fields.Float('Price')
    bought = fields.Boolean('Bought')
    task_id = fields.Many2one('todo.task', 'Task')

    @api.constrains('price')
    def _check_price_negative(self):
        for gift in self:
            if gift.price <= 0:
                raise exceptions.ValidationError('The price must be positive !')

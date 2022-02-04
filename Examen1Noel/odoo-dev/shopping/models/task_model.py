from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)


class Task(models.Model):
    _inherit = ['todo.task']

    gift_ids = fields.One2many('gift', 'task_id')
    totalCost = fields.Float('Total Cost', compute='_compute_total_cost', store=True)

    @api.depends('gift_ids')
    def _compute_total_cost(self):
        for order in self:
            amount_untaxed = 0.0
            for line in order.gift_ids:
                amount_untaxed += line.price

            order.update({
                'totalCost': amount_untaxed,
            })

    def all_buy(self):
        for order in self:
            for line in order.gift_ids:
                line.bought = True
            order.is_done = True

    def cancel(self):
        for order in self:
            for line in order.gift_ids:
                line.bought = False
            order.is_done = False

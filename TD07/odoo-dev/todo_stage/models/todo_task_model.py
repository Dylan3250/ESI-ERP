from odoo import models, fields


class TodoTask(models.Model):
    _inherit = 'todo.task'

    effort_estimate = fields.Integer('Estimate time')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')
    # desc = fields.Text('Description', help="What is the task?")
    desc = fields.Char('Description', help="What is the task?")

    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'), ('done', 'Closed')], default='draft')
    docs = fields.Html('Documentation')

    date_created = fields.Datetime(
        'Create Date and Time',
        default=lambda self: fields.Datetime.now())

    image = fields.Binary('Image')

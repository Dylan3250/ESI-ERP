from odoo import models, fields, exceptions


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

    def set_to_open(self):
        self.state = 'open'

    def set_to_closed(self):
        self.state = 'done'

    def set_to_draft(self):
        self.state = 'draft'

    user_todo_count = fields.Integer('User To-Do Count', compute='_compute_user_todo_count')

    def _compute_user_todo_count(self):
        self.user_todo_count = self.search_count([('user_id', '=', self.user_id.id)])

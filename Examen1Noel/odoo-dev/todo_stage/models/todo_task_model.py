from odoo import models, fields, api, exceptions


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

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

    @api.onchange('user_id')
    def _onchange_user_id(self):
        self.team_ids = None
        return {
            'warning': {
                'title': 'Responsible User Reset',
                'message': 'Please choose a new Team.',
            }
        }

    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise exceptions.ValidationError('Title must have 5 chars!')

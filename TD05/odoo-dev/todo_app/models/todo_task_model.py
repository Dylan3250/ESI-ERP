from odoo import models, fields


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char('Name', help="What needs to be done?", required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    date_deadline = fields.Date('Dateline')
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Team')


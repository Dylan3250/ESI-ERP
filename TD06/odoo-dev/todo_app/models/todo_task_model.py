from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char('Name', help="What needs to be done?", required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    date_deadline = fields.Date('Dateline')
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Team')

    def do_clear_done(self):
        if self.active:
            self.active = False
            _logger.info('============= Do clear done here : %s', __name__)
        else:
            raise exceptions.Warning("La tache est déjà inactive")

    # Se lance à chaque (ré-)écriture (quand on modifie une tâche par exemple)
    def write(self, vals):
        if not 'active' in vals:
            vals['active'] = True
            _logger.info('============= Write here : %s', __name__)
        return super(TodoTask, self).write(vals)

    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, is_done={self.is_done}, active={self.active}, data_deadline={self.date_deadline}, user_name={self.user_id.name}, team_count={len(self.team_ids)})"

    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count([('name', '=like', u"Copie de {}%".format(self.name))])

        if not copied_count:
            new_name = u"Copie de {}".format(self.name)
        else:
            new_name = u"Copie de {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(TodoTask, self).copy(default)

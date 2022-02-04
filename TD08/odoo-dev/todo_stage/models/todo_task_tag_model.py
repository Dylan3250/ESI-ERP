from odoo import models, fields


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char('Tag Name')
    task_ids = fields.Many2many('todo.task', string='Tasks')

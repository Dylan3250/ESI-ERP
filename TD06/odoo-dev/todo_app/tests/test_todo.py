from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestTodo, self).setUp(*args, **kwargs)
        # Création d'un nouvel utilisateur pour les tests
        self.fresh_user = self.env['res.users'].create({
            'login': 'bob',
            'name': "Bob Bobman",
        })
        # Recherche de l'utilisateur avec les droits suffisants
        # sur le module
        self.task_manager = self.env.ref('todo_app.task_manager')

    def test_create(self):
        # Todo = self.env['todo.task']
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.is_done, False)
        self.assertEqual(task.active, True)
        self.assertEqual(task.date_deadline, False)
        # self.assertEqual(task.user_id, self.env.user)
        self.assertEqual(len(task.team_ids), 0)

    def test_clear_done(self):
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertFalse(task.active)

    def test_clear_done_exception(self):
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()

        with self.assertRaises(Exception):
            task.do_clear_done()

    def test_copy_once(self):
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        copy = task.copy()
        self.assertEqual(copy.name, 'Copie de Test Task')

    def test_copy_twice(self):
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        first_copy = task.copy()
        second_copy = task.copy()
        self.assertEqual(first_copy.name, 'Copie de Test Task')
        self.assertEqual(second_copy.name, 'Copie de Test Task (1)')

    def test_record_rule(self):
        Todo = self.env['todo.task'].with_user(self.fresh_user)

        with self.assertRaises(Exception):
            Todo.create({'name': 'New Task'})

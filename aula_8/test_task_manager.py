import unittest
from io import StringIO
import sys
from task_manager import Task, TaskList


class TestTaskManager(unittest.TestCase):

    def test_task_init(self):
        task = Task(1, "Finish Assignment", "Complete the Python assignment")
        self.assertEqual(task.index, 1)
        self.assertEqual("Finish Assignment", task.title)
        self.assertEqual("Complete the Python assignment", task.description)
        self.assertFalse(task.done)

    def test_task_mark_done(self):
        task = Task(1, "Finish Assignment", "Complete the Python assignment")
        task.mark_done()
        self.assertTrue(task.done)

    def test_task_list_add_task(self):
        task_list = TaskList()
        task = Task(1, "Finish Assignment", "Complete the Python assignment")
        task_list.add_task(task)
        self.assertEqual(1, len(task_list.tasks))
        self.assertEqual(2, task_list.get_task_next_available_index())

    def test_task_list_delete_task(self):
        task_list = TaskList()
        task1 = Task(1, "Finish Assignment", "Complete the Python assignment")
        task2 = Task(2, "Study for Exam", "Review the course material")
        task_list.add_task(task1)
        task_list.add_task(task2)

        deleted_task = task_list.delete_task(0)
        self.assertEqual(1, deleted_task.index)
        self.assertEqual(1, len(task_list.tasks))
        self.assertEqual(1, task_list.tasks[0].index)
        self.assertEqual(2, task_list.get_task_next_available_index())

    def test_task_list_list_tasks(self):
        task_list = TaskList()
        task1 = Task(1, "Finish Assignment", "Complete the Python assignment", title_format="capitalize")
        task2 = Task(2, "Study for Exam", "Review the course material", title_format="title")
        task_list.add_task(task1)
        task_list.add_task(task2)

        expected_output = (
            "Task 1\nTitle: Finish Assignment\nDescription: Complete the Python assignment\nDone: False\n"
            "------------------------------\n"
            "Task 2\nTitle: Study for Exam\nDescription: Review the course material\nDone: False\n"
            "------------------------------"
        )

        original_stdout = sys.stdout
        sys.stdout = StringIO()
        task_list.list_tasks()
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        self.assertEqual(output.strip(), expected_output)


if __name__ == "__main__":
    unittest.main()

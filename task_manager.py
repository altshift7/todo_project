# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.completed = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.completed.append(task)

    def get_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        return self.completed

class TaskTracker:
    def __init__(self):
        self.tasks = []
        

    def add(self, task):
        self.tasks.append(task)


    def list_incomplete(self):
        return self.tasks

    def mark_completed(self, index):
        del self.tasks[index]

    
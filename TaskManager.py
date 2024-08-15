import datetime
class Task:
    def __init__(self, task_name: str, description: str, due_date: str, priority_level, completion_status):
        """
        Parameters
		    ----------
			  task_name: str
				  the name of the task to be added to the task manager
			  description: str
				  the description of the task
			  due_date: str
				  the deadline of the task
			  priority_level: str
				  the level of priority (low, medium, high)
			  completion_status: float
				  the status of the task (% complete)
        """
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.priority_level = priority_level
        self.completion_status = completion_status

    def set_description(self, new_description):
        

    def set_priority(self, new_priority):
        

    def set_completion_status(self, new_status):
        

class TaskManager(Task):
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        

    def edit_task(self, task_name, **kwargs):
        

    def delete_task(self, task_name):
        

    def view_tasks(self):
        

    def sort_tasks_by_priority(self):
        

    def get_overdue_tasks(self):
        

class Reminder(Task):
    def __init__(self, task_name, description, due_date, priority_level, completion_status, time_until_deadline, notifications):
        super().__init__(task_name, description, due_date, priority_level, completion_status)
        self.time_until_deadline = time_until_deadline
        self.notifications = notifications

    def generateReminder(self):
        

    def displayNotification(self):
        

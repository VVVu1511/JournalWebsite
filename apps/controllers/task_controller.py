from apps.models.task import Task
class TaskController:
    def __init__(self, list_task: list[Task]):
        self.__list_task = list_task
    def __str__(self):
        #draw the table
        return '\n'.join(self.__list_task)
    def add_new_task(self,task: Task):
        self.list_task.append(task)
    def view_list_tasks(self):
        print(self)
    def change_attribute_tasks(self,task_number: int,field: int,new_data):
        match field:
            case 1:
                self.__list_task[task_number].set_description(new_data)
            case 2:
                self.__list_task[task_number].set_deadline(new_data)
            case 3:
                self.__list_task[task_number].set_state(new_data)
    def delete_task(self,task_number: int):
        del self.__list_task[task_number]
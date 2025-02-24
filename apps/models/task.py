

class Task:
    def __init__(self,description,deadline,state):   
        self.__description = description
        self.__deadline = deadline
        self.__state = state
    def __str__(self):
        return f'{self.description} | {self.deadline} | {self.state}'
    def set_description(self,description):
        self.__description = description
    def set_deadline(self,deadline):
        self.__deadline = deadline
    def set_state(self,state):
        self.__state = state
        
    
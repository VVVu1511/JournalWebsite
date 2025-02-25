from flask import Flask,jsonify,request
from models.database import TaskManager
class API:
    def __init__(self):
        self.__app = Flask(__name__)
        self.__task_manager = TaskManager()
        
        self.__app.add_url_rule('/','get_list',self.get_list,methods = ['GET'])
        self.__app.add_url_rule('/add_task','add_task',self.add_task,methods = ['POST'])
    
    def get_list(self):
        return 'Hello World'

    def add_task(self):
        self.__task_manager.add_values(request.json['description'],request.json['deadline'],request.json['state'])
    
    def run(self,host="127.0.0.1",port = 5000):
        self.__app.run(host=host,port=port)
        
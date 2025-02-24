import sqlite3
from flask import Flask
class TaskManager:
    def __init__(self):
        self.__con = sqlite3.connect('tasks.db')
        self.__cur = self.__con.cursor()
        self.create_table()
        
    def __str__(self):
        return '\n'.join(str(row) for row in self.__cur.execute("SELECT * from tasks").fetchall())
    
    def __del__(self):
        self.__con.close()
    
    def create_table(self,table_name='TaskManager'):
        self.__cur.execute("""CREATE TABLE if not exists tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            deadline TEXT,
            state TEXT
        )""")
        self.__con.commit()
        
    def add_values(self,id = 0,description = '',deadline = '',state = ''):    
        self.__cur.execute("""
        INSERT INTO tasks 
        values (?,?,?,?)    
    """,(id,description,deadline,state))
        self.__con.commit()

    def remove_values(self,id_list: list):
        for id in id_list:
            self.__cur.execute("DELETE FROM tasks WHERE id = (?)",(id,))
        self.__con.commit()
        
    def update_value(self,select_id: int,field: str,new_data):
        self.__cur.execute("UPDATE tasks set (?) = (?) where id = (?)",(field,new_data,select_id,))
        self.__con.commit()
    
    def mark_completed(self,select_id: int):
        self.__cur.execute("UPDATE tasks set state = 'Done' where id = (?)",(select_id,))
        self.__con.commit()
    
    def search_tasks(self,id,description = '',deadline = '',state = ''):
        return '\n'.join(str(row) for row in self.__cur.execute("""SELECT * 
                        from tasks
                        where id = (?) 
                        and description = (?)
                        and deadline = (?)
                        and state = (?)""",(id,description,deadline,state,)
                        ).fetchall())
    
    
def test():
    # test = TaskManager()
    
    # test.add_values(1,'Testing','25-2-2025','Undone')
    # test.add_values(2,'Solving Math','27-3-2025','Done')
    # test.mark_completed(1)
    # test.update_value(1,"deadline","25-5-2025")
    #test.remove_values([1,2])
    # print(test)
    print('Hello World!')


if __name__ == '__main__':
    test()
from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class TaskLists(Base):
    __tablename__ = "TaskLists"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    deadline = Column(DateTime)
    state = Column(String, nullable=False, default="pending")

DATABASE_URL = 'sqlite:///TaskLists.db'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

def add_task():
    deadline_date = datetime.strptime("01-03-2025", "%d-%m-%Y")  
    task = TaskLists(description='Vu', deadline=deadline_date)
    session.add(task)
    session.commit()

add_task()

result = session.execute(text("SELECT * FROM TaskLists"))
for row in result:
    print(row)

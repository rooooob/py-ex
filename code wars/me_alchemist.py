from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#print(rows)

end = False
while not end:
    print("1) Today's tasks")
    print("2) Add task")
    print("0) Exit")

    user = input()
    if user == '0':
        print("\nBye!")
        break

    elif user == '1':
        rows = session.query(Task).all()
        if len(rows) == 0:
           print("")
           print("Today:")
           print("Nothing to do!\n")
          
        else: 
            print("")
            print("Today:")
            for x in range(len(rows)-1):
                print(f"{rows[x].id}. {rows[x].task}")
            print("")

    elif user == '2':
        print("")
        print("Enter task")
        task = input()
        new_row = Task(task=task)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
        print("")
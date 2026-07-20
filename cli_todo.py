tasks = []
class Task:
    def __init__(self,task,time):
        self.task = task
        self.time = time

    def __str__(self):
        return  f"{self.task} - {self.time}"
   
    def __repr__(self):
        return f"{self.task} - {self.time}"

def askuser():
    while True:
        user_input = input("what do you want to do? 1.enter task , 2.remove task , 3.view task 4.exit :")                  
        if user_input == "1":
            task_name = input("enter the task: ")
            task_time = input("enter the time: ")

            task = Task(task_name,task_time)
            tasks.append(task)
        elif user_input == "3":
            for task in tasks:
                print(task)
        
        elif user_input == "4":
            break
askuser()

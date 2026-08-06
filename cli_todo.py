import json
import os

tasks = []


class Task:

    def __init__(self, task, time, completed=False):
        self.task = task
        self.time = time
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.task} - {self.time}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "task": self.task,
            "time": self.time,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task"],
            data["time"],
            data["completed"]
        )


# ---------------- SAVE ----------------

def save_tasks():

    dict_tasks = []

    for task in tasks:
        dict_tasks.append(task.to_dict())

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(dict_tasks, file, indent=4)


# ---------------- LOAD ----------------

def load_tasks():

    if not os.path.exists("tasks.json"):
        return

    with open("tasks.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        tasks.append(Task.from_dict(item))


# ---------------- DISPLAY ----------------

def display_tasks():

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(index, task)


# ---------------- ADD ----------------

def add_task():

    task_name = input("Enter task: ")
    task_time = input("Enter time: ")

    task = Task(task_name, task_time)

    tasks.append(task)

    save_tasks()

    print("Task added successfully.")


# ---------------- DELETE ----------------

def del_tasks():

    if not tasks:
        print("No tasks available.")
        return

    display_tasks()

    try:

        userchoice = int(input("Enter task number to remove: ")) - 1

        tasks.pop(userchoice)

        save_tasks()

        print("Task removed successfully.")

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Invalid task number.")


# ---------------- COMPLETE ----------------

def complete_task():

    if not tasks:
        print("No tasks available.")
        return

    display_tasks()

    try:

        userchoice = int(input("Enter completed task number: ")) - 1

        if tasks[userchoice].completed:
            print("Task already completed.")

        else:
            tasks[userchoice].completed = True
            save_tasks()
            print("Task marked as completed.")

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Invalid task number.")


# ---------------- MENU ----------------

def askuser():

    while True:

        print("\n====== TO DO APP ======")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Mark Completed")
        print("5. Exit")

        user_input = input("Enter choice: ")

        if user_input == "1":
            add_task()

        elif user_input == "2":
            del_tasks()

        elif user_input == "3":
            display_tasks()

        elif user_input == "4":
            complete_task()

        elif user_input == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


# ---------------- PROGRAM START ----------------

load_tasks()
askuser()
from storage import tasks, save_tasks
from datetime import datetime
from task import Task


# ---------------- DISPLAY ----------------

def display_tasks():

    if not tasks:
        print("\nNo tasks available.")
        return

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_tasks = sorted(
        tasks,
        key=lambda task: (
            task.completed,
            priority_order.get(task.priority, 2),
            task.due_time
        )
    )

    print("\n========== TASKS ==========")

    for task in sorted_tasks:
        print(task)

    print("===========================")


# ---------------- ADD ----------------

def add_task():

    while True:

        task_name = input("Enter task: ").strip()

        if task_name:
            break

        print("Task name cannot be empty.")

    due_time = get_due_time()

    priority = get_priority()

    if not tasks:
        new_id = 1
    else:
        new_id = max(task.id for task in tasks) + 1

    task = Task(
        new_id,
        task_name,
        due_time,
        priority=priority
    )

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
        userchoice = int(
            input("Enter task ID to remove: ")
        )

    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:

        if task.id == userchoice:

            tasks.remove(task)

            save_tasks()

            print("Task removed successfully.")
            return

    print("Invalid task ID.")


# ---------------- COMPLETE ----------------

def complete_task():

    if not tasks:
        print("No tasks available.")
        return

    display_tasks()

    try:
        userchoice = int(
            input("Enter task ID to complete: ")
        )

    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:

        if task.id == userchoice:

            if task.completed:
                print("Task already completed.")
                return

            task.completed = True

            save_tasks()

            print("Task marked as completed.")
            return

    print("Invalid task ID.")


# ---------------- UPDATE ----------------

def update_task():

    if not tasks:
        print("No tasks available.")
        return

    display_tasks()

    try:
        userchoice = int(
            input("Enter task ID to update: ")
        )

    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:

        if task.id != userchoice:
            continue

        print("\nWhat do you want to update?")
        print("1. Task name")
        print("2. Due date and time")
        print("3. Priority")

        choice = input("Enter choice: ")

        # Task name
        if choice == "1":

            while True:

                new_name = input(
                    "Enter new task name: "
                ).strip()

                if new_name:
                    task.task = new_name
                    break

                print("Task name cannot be empty.")

        # Due time
        elif choice == "2":

            task.due_time = get_due_time()

            # New due time means the reminder
            # should be allowed to trigger again.
            task.reminder_sent = False

        # Priority
        elif choice == "3":

            task.priority = get_priority()

        else:

            print("Invalid choice.")
            return

        save_tasks()

        print("Task updated successfully.")
        return

    print("Invalid task ID.")


# ---------------- DUE TIME ----------------

def get_due_time():

    while True:

        due_time_string = input(
            "Enter due date and time (YYYY-MM-DD HH:MM): "
        )

        try:
            due_time = datetime.strptime(
                due_time_string,
                "%Y-%m-%d %H:%M"
            )

            if due_time <= datetime.now():
                print("Due time must be in the future.")
                continue

            return due_time

        except ValueError:
            print(
                "Invalid date format. "
                "Use YYYY-MM-DD HH:MM."
            )
# ---------------- PRIORITY ----------------

def get_priority():

    priorities = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }

    while True:

        print("\nPriorities:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        priority_choice = input(
            "Choose priority: "
        )

        if priority_choice in priorities:
            return priorities[priority_choice]

        print(
            "Invalid priority. "
            "Please choose 1, 2, or 3."
        )


# ---------------- MENU ----------------

def askuser():

    while True:

        print("\n====== TO DO APP ======")

        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Mark Completed")
        print("5. Exit")
        print("6. Update Task")

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

        elif user_input == "6":
            update_task()

        else:
            print("Invalid choice.")
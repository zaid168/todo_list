import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from storage import tasks, save_tasks
from task import Task


class TodoApp:

    def __init__(self, root):

        self.root = root
        self.root.title("TODO App")
        self.root.geometry("700x500")

        self.create_widgets()
        self.refresh_tasks()

    # ---------------- GUI ----------------

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="My TODO List",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=20)

        self.task_list = tk.Listbox(
            self.root,
            width=80,
            height=15,
            font=("Arial", 11)
        )

        self.task_list.pack(padx=20, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Add Task",
            width=15,
            command=self.add_task
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Delete Task",
            width=15,
            command=self.delete_task
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Complete Task",
            width=15,
            command=self.complete_task
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Refresh",
            width=15,
            command=self.refresh_tasks
        ).grid(row=0, column=3, padx=5)

    # ---------------- DISPLAY ----------------

    def refresh_tasks(self):

        self.task_list.delete(0, tk.END)

        if not tasks:
            self.task_list.insert(
                tk.END,
                "No tasks available."
            )
            return

        for task in tasks:

            status = "✓" if task.completed else " "

            text = (
                f"[{status}] "
                f"ID: {task.id} | "
                f"{task.priority} | "
                f"{task.task} | "
                f"{task.due_time.strftime('%Y-%m-%d %H:%M')}"
            )

            self.task_list.insert(
                tk.END,
                text
            )

    # ---------------- ADD ----------------

    def add_task(self):

        window = tk.Toplevel(self.root)

        window.title("Add Task")
        window.geometry("400x350")

        tk.Label(
            window,
            text="Task name:"
        ).pack(pady=5)

        task_entry = tk.Entry(
            window,
            width=40
        )

        task_entry.pack()

        tk.Label(
            window,
            text="Due time (YYYY-MM-DD HH:MM):"
        ).pack(pady=5)

        time_entry = tk.Entry(
            window,
            width=40
        )

        time_entry.pack()

        tk.Label(
            window,
            text="Priority:"
        ).pack(pady=5)

        priority_var = tk.StringVar(
            value="Medium"
        )

        priority_menu = tk.OptionMenu(
            window,
            priority_var,
            "High",
            "Medium",
            "Low"
        )

        priority_menu.pack()

        def save_new_task():

            task_name = task_entry.get().strip()

            if not task_name:
                messagebox.showerror(
                    "Error",
                    "Task name cannot be empty."
                )
                return

            try:

                due_time = datetime.strptime(
                    time_entry.get(),
                    "%Y-%m-%d %H:%M"
                )

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Invalid date format."
                )
                return

            if due_time <= datetime.now():

                messagebox.showerror(
                    "Error",
                    "Due time must be in the future."
                )
                return

            if not tasks:
                new_id = 1
            else:
                new_id = max(
                    task.id for task in tasks
                ) + 1

            new_task = Task(
                new_id,
                task_name,
                due_time,
                priority=priority_var.get()
            )

            tasks.append(new_task)

            save_tasks()

            self.refresh_tasks()

            window.destroy()

            messagebox.showinfo(
                "Success",
                "Task added successfully."
            )

        tk.Button(
            window,
            text="Add Task",
            command=save_new_task
        ).pack(pady=20)

    # ---------------- DELETE ----------------

    def delete_task(self):

        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a task first."
            )
            return

        index = selected[0]

        if index >= len(tasks):
            return

        task = tasks[index]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete '{task.task}'?"
        )

        if not confirm:
            return

        tasks.remove(task)

        save_tasks()

        self.refresh_tasks()

    # ---------------- COMPLETE ----------------

    def complete_task(self):

        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a task first."
            )
            return

        index = selected[0]

        if index >= len(tasks):
            return

        task = tasks[index]

        if task.completed:

            messagebox.showinfo(
                "Info",
                "Task is already completed."
            )
            return

        task.completed = True

        save_tasks()

        self.refresh_tasks()


# ---------------- START APP ----------------

if __name__ == "__main__":

    root = tk.Tk()

    app = TodoApp(root)

    root.mainloop()
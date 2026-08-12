import threading

from storage import load_tasks
from notification import check_reminders
from gui import TodoApp

import tkinter as tk


def main():

    load_tasks()

    reminder_thread = threading.Thread(
        target=check_reminders,
        daemon=True
    )

    reminder_thread.start()

    root = tk.Tk()

    app = TodoApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
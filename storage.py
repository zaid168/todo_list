import json
import os

from task import Task


tasks = []


def save_tasks():

    data = []

    for task in tasks:
        data.append(task.to_dict())

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_tasks():

    if not os.path.exists("tasks.json"):
        return

    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Could not load tasks.json. Starting with empty task list.")
        return

    tasks.clear()

    for item in data:
        tasks.append(Task.from_dict(item))
from datetime import datetime


class Task:

    def __init__(
        self,
        id,
        task,
        due_time,
        completed=False,
        priority="Medium",
        reminder_sent=False
    ):
        self.id = id
        self.task = task
        self.due_time = due_time
        self.completed = completed
        self.priority = priority
        self.reminder_sent = reminder_sent

    def __str__(self):

        status = "✓" if self.completed else " "

        overdue = ""

        if not self.completed and self.due_time < datetime.now():
            overdue = " | OVERDUE"

        formatted_time = self.due_time.strftime("%Y-%m-%d %H:%M")

        return (
            f"[{status}] "
            f"ID:{self.id} | "
            f"{self.priority} | "
            f"{self.task} - "
            f"{formatted_time}"
            f"{overdue}"
        )

    def __repr__(self):
        return self.__str__()

    def to_dict(self):

        return {
            "id": self.id,
            "task": self.task,
            "due_time": self.due_time.isoformat(),
            "completed": self.completed,
            "priority": self.priority,
            "reminder_sent": self.reminder_sent
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["id"],
            data["task"],
            datetime.fromisoformat(data["due_time"]),
            data.get("completed", False),
            data.get("priority", "Medium"),
            data.get("reminder_sent", False)
        )
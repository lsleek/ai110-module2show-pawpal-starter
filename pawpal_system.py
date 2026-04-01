import datetime

class Task:
    def __init__(self, description: str, time: int, frequency: str, priority: int = 1, completed: bool = False, due_date: datetime.date = None):
        """Initialize a Task with description, time, frequency, priority, completion status, and due date."""
        self.description = description
        self.time = time  # duration in minutes
        self.frequency = frequency  # e.g., 'daily', 'weekly'
        self.priority = priority  # higher number means higher priority
        self.completed = completed  # completion status
        self.due_date = due_date if due_date else datetime.date.today()

    def mark_complete(self):
        """Mark the task as completed by setting completed to True."""
        self.completed = True

class Pet:
    def __init__(self, name: str, species: str):
        """Initialize a Pet with name and species, and an empty list of tasks."""
        self.name = name
        self.species = species
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        """Add a task to the pet's list of tasks."""
        self.tasks.append(task)

    def get_tasks(self) -> list[Task]:
        """Return the list of tasks associated with the pet."""
        return self.tasks

    def mark_task_complete(self, task: Task):
        """Mark a task as complete and create a new recurring task if applicable."""
        task.completed = True
        if task.frequency == "daily":
            new_due = task.due_date + datetime.timedelta(days=1)
            new_task = Task(task.description, task.time, task.frequency, task.priority, False, new_due)
            self.add_task(new_task)
        elif task.frequency == "weekly":
            new_due = task.due_date + datetime.timedelta(weeks=1)
            new_task = Task(task.description, task.time, task.frequency, task.priority, False, new_due)
            self.add_task(new_task)

class Owner:
    def __init__(self, name: str):
        """Initialize an Owner with name and an empty list of pets."""
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Return a list of all tasks from all pets owned by the owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks

    def get_tasks_by_status(self, completed: bool) -> list[Task]:
        """Return tasks filtered by completion status."""
        return [t for t in self.get_all_tasks() if t.completed == completed]

    def get_tasks_by_pet(self, pet_name: str) -> list[Task]:
        """Return tasks for a specific pet by name."""
        for p in self.pets:
            if p.name == pet_name:
                return p.get_tasks()
        return []

class Scheduler:
    def __init__(self, owner: Owner, available_time: int):  # available_time in hours
        """Initialize a Scheduler with an owner and available time in hours, converted to minutes."""
        self.owner = owner
        self.available_time_minutes = available_time * 60  # convert to minutes

    def generate_schedule(self) -> list[Task]:
        """Generate a schedule of tasks sorted by priority and time, fitting within available time."""
        tasks = [t for t in self.owner.get_all_tasks() if not t.completed]
        # Sort by priority (higher first), then by duration (shorter first)
        tasks.sort(key=lambda t: (-t.priority, t.time))
        schedule = []
        total_time = 0
        for task in tasks:
            if total_time + task.time <= self.available_time_minutes:
                schedule.append(task)
                total_time += task.time
        return schedule

    def sort_tasks_by_time(self) -> list[Task]:
        """Sort tasks by their duration time in ascending order."""
        tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda t: t.time)

    def detect_conflicts(self) -> list[str]:
        """Detect potential conflicts by checking for multiple tasks on the same due date."""
        tasks = self.owner.get_all_tasks()
        due_dates = {}
        for t in tasks:
            if t.due_date in due_dates:
                due_dates[t.due_date].append(t)
            else:
                due_dates[t.due_date] = [t]
        conflicts = []
        for date, ts in due_dates.items():
            if len(ts) > 1:
                task_names = [t.description for t in ts]
                conflicts.append(f"Multiple tasks on {date}: {task_names}")
        return conflicts
class Task:
    def __init__(self, description: str, time: int, frequency: str, priority: int = 1, completed: bool = False):
        """Initialize a Task with description, time, frequency, priority, and completion status."""
        self.description = description
        self.time = time  # duration in minutes
        self.frequency = frequency  # e.g., 'daily', 'weekly'
        self.priority = priority  # higher number means higher priority
        self.completed = completed  # completion status

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

class Scheduler:
    def __init__(self, owner: Owner, available_time: int):  # available_time in hours
        """Initialize a Scheduler with an owner and available time in hours, converted to minutes."""
        self.owner = owner
        self.available_time_minutes = available_time * 60  # convert to minutes

    def generate_schedule(self) -> list[Task]:
        """Generate a schedule of tasks sorted by priority and time, fitting within available time."""
        tasks = self.owner.get_all_tasks()
        # Sort by priority (higher first), then by duration (shorter first)
        tasks.sort(key=lambda t: (-t.priority, t.time))
        schedule = []
        total_time = 0
        for task in tasks:
            if total_time + task.time <= self.available_time_minutes:
                schedule.append(task)
                total_time += task.time
        return schedule
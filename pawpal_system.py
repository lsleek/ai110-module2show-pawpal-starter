class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def get_info(self) -> str:
        return f"{self.name} is a {self.species}"


class Owner:
    def __init__(self, name: str, preferences: list[str] = None):
        self.name = name
        self.preferences = preferences or []

    def update_preferences(self, new_preferences: list[str]):
        self.preferences = new_preferences


class Task:
    def __init__(self, title: str, duration: int, priority: int):
        self.title = title
        self.duration = duration
        self.priority = priority

    def is_high_priority(self) -> bool:
        return self.priority > 3


class Scheduler:
    def __init__(self, tasks: list[Task], available_time: int):
        self.tasks = tasks
        self.available_time = available_time

    def generate_schedule(self) -> list:
        # Placeholder for scheduling logic
        pass
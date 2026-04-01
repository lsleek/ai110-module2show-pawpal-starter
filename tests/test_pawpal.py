import pytest
import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_creation_with_due_date():
    """Verify that Task is created with correct due_date."""
    today = datetime.date.today()
    task = Task("Walk the dog", 30, "daily", due_date=today)
    assert task.due_date == today
    assert not task.completed

def test_task_mark_complete_changes_status():
    """Verify that calling mark_complete() changes the task's completed status to True."""
    task = Task("Walk the dog", 30, "daily")
    assert not task.completed  # Initially False
    task.mark_complete()
    assert task.completed  # Should be True after marking complete

def test_pet_add_task_increases_task_count():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = Pet("Buddy", "Dog")
    initial_count = len(pet.tasks)
    task = Task("Feed the pet", 10, "daily")
    pet.add_task(task)
    assert len(pet.tasks) == initial_count + 1

def test_sort_tasks_by_time():
    """Verify that tasks are sorted by duration in ascending order."""
    owner = Owner("John")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)
    
    task1 = Task("Short task", 10, "daily")
    task2 = Task("Long task", 30, "daily")
    task3 = Task("Medium task", 20, "daily")
    
    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)
    
    scheduler = Scheduler(owner, 2)
    sorted_tasks = scheduler.sort_tasks_by_time()
    
    assert len(sorted_tasks) == 3
    assert sorted_tasks[0].time == 10
    assert sorted_tasks[1].time == 20
    assert sorted_tasks[2].time == 30

def test_filter_tasks_by_status():
    """Verify filtering tasks by completion status."""
    owner = Owner("John")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)
    
    task1 = Task("Task 1", 10, "daily")
    task2 = Task("Task 2", 20, "daily")
    task2.mark_complete()
    
    pet.add_task(task1)
    pet.add_task(task2)
    
    incomplete = owner.get_tasks_by_status(False)
    complete = owner.get_tasks_by_status(True)
    
    assert len(incomplete) == 1
    assert len(complete) == 1
    assert incomplete[0].description == "Task 1"
    assert complete[0].description == "Task 2"

def test_filter_tasks_by_pet():
    """Verify filtering tasks by pet name."""
    owner = Owner("John")
    pet1 = Pet("Buddy", "Dog")
    pet2 = Pet("Whiskers", "Cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    
    task1 = Task("Dog task", 10, "daily")
    task2 = Task("Cat task", 20, "daily")
    
    pet1.add_task(task1)
    pet2.add_task(task2)
    
    buddy_tasks = owner.get_tasks_by_pet("Buddy")
    whiskers_tasks = owner.get_tasks_by_pet("Whiskers")
    
    assert len(buddy_tasks) == 1
    assert len(whiskers_tasks) == 1
    assert buddy_tasks[0].description == "Dog task"
    assert whiskers_tasks[0].description == "Cat task"

def test_recurring_task_creation():
    """Verify that marking a daily task complete creates a new task for the next day."""
    pet = Pet("Buddy", "Dog")
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    
    task = Task("Walk", 30, "daily", due_date=today)
    pet.add_task(task)
    
    initial_count = len(pet.tasks)
    pet.mark_task_complete(task)
    
    assert len(pet.tasks) == initial_count + 1
    new_task = pet.tasks[-1]  # The newly added task
    assert new_task.description == "Walk"
    assert new_task.due_date == tomorrow
    assert not new_task.completed

def test_conflict_detection():
    """Verify that conflicts are detected for multiple tasks on the same date."""
    owner = Owner("John")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)
    
    today = datetime.date.today()
    task1 = Task("Task 1", 10, "daily", due_date=today)
    task2 = Task("Task 2", 20, "daily", due_date=today)
    
    pet.add_task(task1)
    pet.add_task(task2)
    
    scheduler = Scheduler(owner, 2)
    conflicts = scheduler.detect_conflicts()
    
    assert len(conflicts) == 1
    assert "Multiple tasks on" in conflicts[0]
    assert str(today) in conflicts[0]

def test_schedule_generation_excludes_completed():
    """Verify that schedule generation only includes incomplete tasks."""
    owner = Owner("John")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)
    
    task1 = Task("Incomplete task", 30, "daily")
    task2 = Task("Completed task", 30, "daily")
    task2.mark_complete()
    
    pet.add_task(task1)
    pet.add_task(task2)
    
    scheduler = Scheduler(owner, 2)  # 120 minutes
    schedule = scheduler.generate_schedule()
    
    assert len(schedule) == 1
    assert schedule[0].description == "Incomplete task"

def test_edge_case_no_tasks():
    """Verify behavior with no tasks."""
    owner = Owner("John")
    scheduler = Scheduler(owner, 2)
    
    sorted_tasks = scheduler.sort_tasks_by_time()
    conflicts = scheduler.detect_conflicts()
    schedule = scheduler.generate_schedule()
    
    assert sorted_tasks == []
    assert conflicts == []
    assert schedule == []

def test_edge_case_pet_no_tasks():
    """Verify filtering for pet with no tasks."""
    owner = Owner("John")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)
    
    tasks = owner.get_tasks_by_pet("Buddy")
    assert tasks == []
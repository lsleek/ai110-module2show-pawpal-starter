import pytest
from pawpal_system import Task, Pet

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
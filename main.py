from pawpal_system import Owner, Pet, Task, Scheduler
import datetime

# Create an Owner
owner = Owner("John Doe")

# Create at least two Pets
pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Whiskers", "Cat")

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Add tasks with different times (out of order)
task1 = Task("Morning walk", 30, "daily", priority=5)  # 30 minutes
task2 = Task("Feed breakfast", 10, "daily", priority=4)  # 10 minutes
task3 = Task("Playtime", 45, "daily", priority=3)  # 45 minutes
task4 = Task("Evening walk", 20, "daily", priority=2)  # 20 minutes

pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)
pet1.add_task(task4)

# Test sorting by time
scheduler = Scheduler(owner, available_time=2)
sorted_tasks = scheduler.sort_tasks_by_time()
print("Tasks sorted by time:")
for task in sorted_tasks:
    print(f"- {task.description} ({task.time} minutes)")

# Test filtering
completed_tasks = owner.get_tasks_by_status(True)
incomplete_tasks = owner.get_tasks_by_status(False)
print(f"\nCompleted tasks: {len(completed_tasks)}")
print(f"Incomplete tasks: {len(incomplete_tasks)}")

buddy_tasks = owner.get_tasks_by_pet("Buddy")
print(f"\nBuddy's tasks: {[t.description for t in buddy_tasks]}")

# Test recurring tasks
print("\nBefore marking complete:")
print(f"Buddy's tasks: {[t.description for t in pet1.get_tasks()]}")
pet1.mark_task_complete(task1)  # Mark morning walk complete
print("After marking 'Morning walk' complete (daily):")
print(f"Buddy's tasks: {[t.description for t in pet1.get_tasks()]}")

# Test conflict detection
# Add another task on same date
today = datetime.date.today()
task5 = Task("Grooming", 15, "daily", priority=1, due_date=today)
pet1.add_task(task5)

conflicts = scheduler.detect_conflicts()
print(f"\nConflicts detected: {conflicts}")

# Generate today's schedule
schedule = scheduler.generate_schedule()
print("\nToday's Schedule:")
for task in schedule:
    print(f"- {task.description} ({task.time} minutes, Priority: {task.priority})")
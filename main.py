from pawpal_system import Owner, Pet, Task, Scheduler

# Create an Owner
owner = Owner("John Doe")

# Create at least two Pets
pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Whiskers", "Cat")

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Add at least three Tasks with different times to those pets
task1 = Task("Morning walk", 30, "daily", priority=5)  # 30 minutes
task2 = Task("Feed breakfast", 10, "daily", priority=4)  # 10 minutes
task3 = Task("Playtime", 45, "daily", priority=3)  # 45 minutes

pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)

# Create Scheduler with available time (e.g., 2 hours = 120 minutes)
scheduler = Scheduler(owner, available_time=2)

# Generate today's schedule
schedule = scheduler.generate_schedule()

# Print "Today's Schedule"
print("Today's Schedule:")
for task in schedule:
    print(f"- {task.description} ({task.time} minutes, Priority: {task.priority})")
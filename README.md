# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Features

PawPal+ includes the following smart features:

- **Task Management**: Add pets and assign care tasks with priorities, durations, and frequencies
- **Intelligent Scheduling**: Generate optimized daily schedules based on available time, task priorities, and completion status
- **Sorting by Time**: Sort tasks by duration for better planning
- **Advanced Filtering**: Filter tasks by completion status or specific pets
- **Recurring Tasks**: Automatic creation of daily/weekly recurring tasks when completed
- **Conflict Detection**: Warn about multiple tasks scheduled on the same date
- **Persistent Sessions**: Data persists across page refreshes using Streamlit session state

## 📸 Demo

<a href="/course_images/ai110/pawpal_demo.png" target="_blank"><img src='/course_images/ai110/pawpal_demo.png' title='PawPal+ App Demo' width='' alt='PawPal+ App Demo' class='center-block' /></a>

## Testing PawPal+

Run the test suite with:
```bash
python3 -m pytest tests/
```

The test suite covers:
- Basic task and pet operations
- Sorting tasks by duration
- Filtering tasks by completion status and pet
- Recurring task creation when marking tasks complete
- Conflict detection for multiple tasks on the same date
- Schedule generation that excludes completed tasks
- Edge cases like no tasks or empty pets

**Confidence Level:** ⭐⭐⭐⭐⭐ (5/5 stars) - All core behaviors are tested with comprehensive coverage including edge cases, and all tests pass consistently. The system handles sorting, filtering, recurring tasks, and conflict detection reliably. 

## Project Structure

- `pawpal_system.py`: Core classes (Task, Pet, Owner, Scheduler) and algorithms
- `app.py`: Streamlit web interface
- `main.py`: Terminal demo of the system
- `tests/test_pawpal.py`: Automated test suite
- `reflection.md`: Project reflection and design decisions

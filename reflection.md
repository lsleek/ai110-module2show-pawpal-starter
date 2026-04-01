# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The initial UML design for PawPal+ includes four main classes: Pet, Owner, Task, and Scheduler. The Pet class holds basic pet information and provides methods to retrieve details. The Owner class manages owner information and preferences. The Task class represents individual care tasks with attributes for title, duration, and priority, along with methods to check priority. The Scheduler class handles the list of tasks and available time, with a method to generate a daily schedule.
```mermaid
classDiagram
    class Task {
        +description: str
        +time: int
        +frequency: str
        +priority: int
        +completed: bool
        +due_date: date
        +__init__(description, time, frequency, priority, completed, due_date)
        +mark_complete(): void
    }
    class Pet {
        +name: str
        +species: str
        +tasks: list[Task]
        +__init__(name, species)
        +add_task(task: Task): void
        +get_tasks(): list[Task]
        +mark_task_complete(task: Task): void
    }
    class Owner {
        +name: str
        +pets: list[Pet]
        +__init__(name)
        +add_pet(pet: Pet): void
        +get_all_tasks(): list[Task]
        +get_tasks_by_status(completed: bool): list[Task]
        +get_tasks_by_pet(pet_name: str): list[Task]
    }
    class Scheduler {
        +owner: Owner
        +available_time_minutes: int
        +__init__(owner, available_time)
        +generate_schedule(): list[Task]
        +sort_tasks_by_time(): list[Task]
        +detect_conflicts(): list[str]
    }

    Owner --> Pet : owns
    Pet --> Task : has
    Scheduler --> Owner : uses
```

**b. Design changes**

- Yes, my design changed significantly during implementation. Initially, I planned for simple classes without advanced features, but as I built the algorithms, I added attributes like `due_date` to the Task class to support recurring tasks, and new methods like `get_tasks_by_status` and `get_tasks_by_pet` to the Owner class for filtering. I also moved the `mark_complete` logic from Task to Pet to handle recurring task creation properly. These changes were necessary to make the system more functional and user-friendly, evolving from a basic scheduler to a smart pet care assistant.

**c. Core User Actions**

The three core actions a user should be able to perform in PawPal+ are: 1. Add a pet: Users can enter basic information about their pet, such as name and species, to set up the pet profile. 2. Schedule a walk/task: Users can add or edit pet care tasks, including specifying the task title, duration in minutes, and priority level. 3. See today's tasks: Users can generate and view a daily schedule of pet care tasks, which considers available time, task priorities, and owner preferences, along with an explanation of the planning logic.

**d. Building Blocks**

- Pet: Attributes - name (string), species (string, e.g., dog, cat). Methods - get_info() (returns pet details).
- Owner: Attributes - name (string), preferences (list of strings, e.g., preferred times). Methods - update_preferences() (modifies preferences).
- Task: Attributes - title (string), duration (int, minutes), priority (int, 1-5). Methods - is_high_priority() (returns bool if priority > 3).
- Scheduler: Attributes - tasks (list of Task objects), available_time (int, hours). Methods - generate_schedule() (creates a daily plan list based on priorities and time).

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- My scheduler considers several key constraints: the available time in hours (converted to minutes), task priorities (higher numbers mean higher priority), and task completion status (only incomplete tasks are scheduled). It also respects the due dates for conflict detection.
- I decided on these constraints based on the project requirements, which emphasized time management, priority handling, and ensuring only relevant tasks are included. Time and priority were the most critical because they directly impact the scheduling algorithm's effectiveness, while completion status ensures the schedule stays current.

**b. Tradeoffs**

- The conflict detection algorithm only checks for multiple tasks scheduled on the same due date, rather than detecting overlapping time slots.
- This tradeoff is reasonable for this scenario because the current system doesn't assign specific start times to tasks, keeping the implementation simple while still alerting users to potential scheduling conflicts on busy days.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI tools extensively throughout the project for design brainstorming (like suggesting algorithm ideas), debugging (identifying why tests failed), and refactoring (simplifying code for readability). For example, I asked Copilot to help implement sorting and filtering methods, generate test cases, and even write documentation.
- The most helpful prompts were specific and contextual, such as "How can I sort a list of Task objects by their time attribute?" or "Why is this test failing and how can I fix it?" These targeted questions led to actionable, high-quality suggestions that saved time and improved code quality.

**b. Judgment and verification**

- One moment where I did not accept an AI suggestion as-is was during the implementation of recurring tasks. The initial approach suggested moving the mark_complete logic entirely to the Owner class, but I kept it in Pet for better encapsulation, as each pet manages its own tasks. I evaluated this by considering the single responsibility principle and testing that the logic worked correctly.
- I evaluated AI suggestions by running the code, checking test results, and ensuring the code remained readable and maintainable. For complex logic, I would break it down and test incrementally.

---

## 4. Testing and Verification

**a. What you tested**

- I tested core behaviors including task creation, pet management, sorting by time, filtering by status and pet, recurring task generation, conflict detection, and schedule generation with time constraints.
- These tests were important because they verify that all algorithmic features work correctly and handle edge cases like empty systems or completed tasks, ensuring the system is reliable for real use.

**b. Confidence**

- I am highly confident (5/5) that the scheduler works correctly because all 11 automated tests pass, covering both happy paths and edge cases. The system consistently handles sorting, filtering, recurring tasks, and conflict detection.
- If I had more time, I would test overlapping time slots (assigning actual start times), multi-pet scheduling conflicts, and user input validation in the UI.

---

## 5. Reflection

**AI Strategy Reflection:**

- The most effective Copilot features were inline chat for code generation and debugging, the terminal tool for running tests and commands, and semantic search for understanding existing code. These helped me implement algorithms quickly and catch issues early.
- One example of rejecting an AI suggestion was when it proposed a complex conflict detection algorithm using time intervals; I simplified it to date-based detection to keep the system lightweight and focused on the core requirements.
- Using separate chat sessions for different phases helped me stay organized by keeping context focused on one aspect at a time, preventing confusion between implementation details.
- As the lead architect collaborating with AI, I learned to guide the tools toward my vision while leveraging their speed for implementation. I make the high-level design decisions, evaluate tradeoffs, and ensure the final system aligns with the project goals, while AI handles the detailed coding and suggestions. This partnership maximizes productivity while maintaining human oversight. 

**a. What went well**

- I'm most satisfied with how the backend logic integrated seamlessly with the Streamlit UI, creating a functional app that actually helps users manage pet care tasks. The step-by-step development process, guided by AI, resulted in a system that's both smart and user-friendly.

**b. What you would improve**

- If I had another iteration, I would improve the UI by adding more interactive features like drag-and-drop task reordering, better error handling for invalid inputs, and perhaps notifications for upcoming tasks. I'd also expand the backend to handle overlapping time slots and multi-pet conflicts more robustly.

**c. Key takeaway**

- One important thing I learned is the value of iterative design and thorough testing when working with AI. AI can accelerate development, but human judgment is crucial for making design decisions that ensure the system is maintainable, user-focused, and aligned with real-world needs. It's about balancing AI's speed with thoughtful architecture.

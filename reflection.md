# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The initial UML design for PawPal+ includes four main classes: Pet, Owner, Task, and Scheduler. The Pet class holds basic pet information and provides methods to retrieve details. The Owner class manages owner information and preferences. The Task class represents individual care tasks with attributes for title, duration, and priority, along with methods to check priority. The Scheduler class handles the list of tasks and available time, with a method to generate a daily schedule.

```mermaid
classDiagram
    class Pet {
        +name: string
        +species: string
        +get_info(): string
    }
    class Owner {
        +name: string
        +preferences: list[string]
        +update_preferences(): void
    }
    class Task {
        +title: string
        +duration: int
        +priority: int
        +is_high_priority(): bool
    }
    class Scheduler {
        +tasks: list[Task]
        +available_time: int
        +generate_schedule(): list
    }
    Owner ||--|| Pet : owns
    Scheduler ||--o{ Task : manages
```

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- The conflict detection algorithm only checks for multiple tasks scheduled on the same due date, rather than detecting overlapping time slots.
- This tradeoff is reasonable for this scenario because the current system doesn't assign specific start times to tasks, keeping the implementation simple while still alerting users to potential scheduling conflicts on busy days.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

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

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

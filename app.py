import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    if 'owner' not in st.session_state:
        st.session_state.owner = Owner(owner_name)
    pet = Pet(pet_name, species)
    st.session_state.owner.add_pet(pet)
    st.success(f"Added pet {pet_name}")

# Display pets
if 'owner' in st.session_state:
    pets = st.session_state.owner.pets
    if pets:
        st.write("Current pets:")
        for p in pets:
            st.write(f"- {p.name} ({p.species})")

st.markdown("### Tasks")
st.caption("Add tasks to a selected pet.")

# Select pet
if 'owner' in st.session_state and st.session_state.owner.pets:
    pet_options = [p.name for p in st.session_state.owner.pets]
    selected_pet = st.selectbox("Select pet to add task to", pet_options)
else:
    st.info("Add a pet first to add tasks.")
    selected_pet = None

if selected_pet:
    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority_str = st.selectbox("Priority", ["low", "medium", "high"], index=2)
        priority = {"low": 1, "medium": 2, "high": 3}[priority_str]

    if st.button("Add task"):
        pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet)
        task = Task(task_title, duration, "daily", priority)
        pet.add_task(task)
        st.success(f"Added task '{task_title}' to {selected_pet}")

# Display tasks
if 'owner' in st.session_state:
    all_tasks = st.session_state.owner.get_all_tasks()
    if all_tasks:
        st.write("Current tasks:")
        for t in all_tasks:
            st.write(f"- {t.description} ({t.time} min, priority {t.priority})")
    else:
        st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
available_time = st.number_input("Available time (hours)", min_value=1, max_value=24, value=2)
st.caption("This button calls your scheduling logic.")

if st.button("Generate schedule"):
    if 'owner' in st.session_state and st.session_state.owner.get_all_tasks():
        scheduler = Scheduler(st.session_state.owner, available_time)
        schedule = scheduler.generate_schedule()
        if schedule:
            st.write("Generated schedule:")
            for t in schedule:
                st.write(f"- {t.description} ({t.time} min)")
        else:
            st.info("No tasks fit in the available time.")
    else:
        st.warning("Add pets and tasks first.")

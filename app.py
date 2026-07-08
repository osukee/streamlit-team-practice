import streamlit as st
import pandas as pd

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="SprintMate",
    page_icon="📋",
    layout="wide"
)

# ==========================
# Sidebar Navigation (PB-01)
# ==========================
st.sidebar.title("📋 SprintMate")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Project Setup",
        "📝 Task Brainstorming",
        "⭐ Task Scoring",
        "📦 Assignment Result"
    ]
)

# ==========================
# Mock Data
# （之后由 data_manager.py 替代）
# ==========================

members = ["Alice", "Bob", "Charlie", "David"]

tasks = [
    {
        "Task":"Homepage",
        "Category":"UI"
    },
    {
        "Task":"Database",
        "Category":"Backend"
    }
]

assignment = {
    "Alice":["Homepage"],
    "Bob":["Database"],
    "Charlie":["Presentation"],
    "David":["Testing"]
}

# ======================================================
# Project Setup (PB-02)
# ======================================================

if page == "🏠 Project Setup":

    st.title("📁 Project Setup")

    project_name = st.text_input("Project Name")

    project_description = st.text_area(
        "Project Description"
    )

    deadline = st.date_input("Deadline")

    st.subheader("Team Members")

    member_input = st.text_input(
        "Enter members separated by commas",
        value="Alice, Bob, Charlie, David"
    )

    if st.button("Save Project"):

        st.success("Project saved successfully!")

        st.write("### Summary")

        st.write("Project:", project_name)
        st.write("Deadline:", deadline)
        st.write("Members:", member_input)

# ======================================================
# Task Brainstorming (PB-05)
# ======================================================

elif page == "📝 Task Brainstorming":

    st.title("📝 Task Brainstorming")

    task_name = st.text_input("Task Name")

    category = st.selectbox(
        "Category",
        [
            "Planning",
            "Development",
            "Design",
            "Research",
            "Presentation",
            "Documentation"
        ]
    )

    description = st.text_area(
        "Description"
    )

    if st.button("Add Task"):

        st.success(f"{task_name} added!")

    st.divider()

    st.subheader("Current Tasks")

    st.dataframe(
        pd.DataFrame(tasks),
        use_container_width=True
    )

# ======================================================
# Task Scoring (PB-08)
# ======================================================

elif page == "⭐ Task Scoring":

    st.title("⭐ Task Scoring")

    selected_task = st.selectbox(
        "Select Task",
        [task["Task"] for task in tasks]
    )

    st.write(f"### Score for: {selected_task}")

    scores = {}

    for member in members:

        scores[member] = st.slider(
            member,
            min_value=1,
            max_value=5,
            value=3
        )

    if st.button("Submit Scores"):

        st.success("Scores submitted!")

        score_df = pd.DataFrame({
            "Member":scores.keys(),
            "Score":scores.values()
        })

        st.dataframe(score_df)

# ======================================================
# Assignment Result (PB-14)
# ======================================================

elif page == "📦 Assignment Result":

    st.title("📦 Assignment Result")

    cols = st.columns(2)

    for i, member in enumerate(members):

        with cols[i % 2]:

            st.subheader(member)

            total_score = 0

            for task in assignment[member]:

                st.checkbox(task, value=False)

                total_score += 3

            st.metric(
                "Workload Score",
                total_score
            )
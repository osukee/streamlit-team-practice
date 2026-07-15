from datetime import date
import statistics
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="SprintMate",
    layout="wide",
)

PAGES = [
    "Project Setup",
    "Task Brainstorming",
    "Task Scoring",
    "Assignment Result",
    "Dashboard",
]

def init_state():
    if "project" not in st.session_state:
        st.session_state.project = {
            "name": "",
            "description": "",
            "deadline": date.today().isoformat(),
        }

    if "members" not in st.session_state:
        st.session_state.members = ["Alice", "Bob", "Charlie", "David"]

    if "tasks" not in st.session_state:
        st.session_state.tasks = [
            {
                "id": 1,
                "name": "Create homepage",
                "category": "Design",
                "description": "Build the first screen for the project.",
            },
            {
                "id": 2,
                "name": "Prepare database",
                "category": "Development",
                "description": "Design the data structure for members and tasks.",
            },
        ]

    if "next_task_id" not in st.session_state:
        st.session_state.next_task_id = 3

    if "scores" not in st.session_state:
        st.session_state.scores = {}

    if "assignments" not in st.session_state:
        st.session_state.assignments = {}


def member_names_from_text(raw_names):
    names = []
    seen = set()

    for name in raw_names.split(","):
        clean_name = name.strip()
        if clean_name and clean_name.lower() not in seen:
            names.append(clean_name)
            seen.add(clean_name.lower())

    return names


def get_task(task_id):
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            return task
    return None


def task_score(task_id, member):
    return st.session_state.scores.get(task_id, {}).get(member)


def task_average(task_id):
    scores = [
        task_score(task_id, member)
        for member in st.session_state.members
        if task_score(task_id, member) is not None
    ]

    if not scores:
        return 0

    return sum(scores) / len(scores)

def task_variance(task_id):
    scores = [
        task_score(task_id, member)
        for member in st.session_state.members
        if task_score(task_id, member) is not None
    ]

    if len(scores) <= 1:
        return 0

    return round(statistics.stdev(scores), 2)

def task_score_status(task_id):
    submitted = sum(
        1
        for member in st.session_state.members
        if task_score(task_id, member) is not None
    )
    total = len(st.session_state.members)
    return submitted, total


def score_table():
    rows = []

    for task in st.session_state.tasks:
        submitted, total = task_score_status(task["id"])
        rows.append(
            {
                "Task": task["name"],
                "Category": task["category"],
                "Average Score": round(task_average(task["id"]), 2),
                "Variance": task_variance(task["id"]),
                "Scores Submitted": f"{submitted}/{total}",
            }
        )

    return pd.DataFrame(rows)


def generate_assignment():
    assignments = {member: [] for member in st.session_state.members}
    workloads = {member: 0.0 for member in st.session_state.members}

    ranked_tasks = sorted(
        st.session_state.tasks,
        key=lambda task: task_average(task["id"]),
        reverse=True,
    )

    for task in ranked_tasks:
        member = min(workloads, key=workloads.get)
        assignments[member].append(task["id"])
        workloads[member] += task_average(task["id"]) or 3

    st.session_state.assignments = assignments


def workload_rows():
    rows = []

    for member in st.session_state.members:
        task_ids = st.session_state.assignments.get(member, [])
        workload = sum(task_average(task_id) or 3 for task_id in task_ids)
        rows.append(
            {
                "Member": member,
                "Assigned Tasks": len(task_ids),
                "Workload Score": round(workload, 2),
            }
        )

    return pd.DataFrame(rows)

def workload_difference():

    workload = workload_rows()

    if workload.empty:
        return 0

    return round(
        workload["Workload Score"].max()
        - workload["Workload Score"].min(),
        2,
    )

def show_sidebar():
    st.sidebar.title("SprintMate")
    page = st.sidebar.radio("Navigation", PAGES)

    st.sidebar.divider()
    st.sidebar.caption("Current project")
    st.sidebar.write(st.session_state.project["name"] or "Not saved yet")
    st.sidebar.write(f"Members: {len(st.session_state.members)}")
    st.sidebar.write(f"Tasks: {len(st.session_state.tasks)}")

    return page


def show_project_setup():
    st.title("Project Setup")
    st.caption("PB-02: Create a group project and define the team context.")

    project = st.session_state.project
    saved_deadline = date.fromisoformat(project["deadline"])

    with st.form("project_setup_form"):
        project_name = st.text_input("Project Name", value=project["name"])
        project_description = st.text_area(
            "Project Description",
            value=project["description"],
        )
        deadline = st.date_input("Deadline", value=saved_deadline)
        member_input = st.text_input(
            "Team Members",
            value=", ".join(st.session_state.members),
            help="Separate member names with commas.",
        )

        submitted = st.form_submit_button("Save Project")

    if submitted:
        members = member_names_from_text(member_input)

        if not project_name.strip():
            st.error("Project name is required.")
        elif not members:
            st.error("Add at least one team member.")
        else:
            st.session_state.project = {
                "name": project_name.strip(),
                "description": project_description.strip(),
                "deadline": deadline.isoformat(),
            }
            st.session_state.members = members
            st.session_state.assignments = {}
            st.success("Project saved.")

    st.subheader("Project Summary")
    summary = {
        "Project": st.session_state.project["name"] or "-",
        "Deadline": st.session_state.project["deadline"],
        "Members": ", ".join(st.session_state.members),
    }
    st.dataframe(pd.DataFrame([summary]), use_container_width=True, hide_index=True)


def show_task_brainstorming():
    st.title("Task Brainstorming")
    st.caption("PB-05: Add tasks that the group needs to complete.")

    with st.form("task_form", clear_on_submit=True):
        task_name = st.text_input("Task Name")
        category = st.selectbox(
            "Category",
            [
                "Planning",
                "Development",
                "Design",
                "Research",
                "Presentation",
                "Documentation",
            ],
        )
        description = st.text_area("Description")
        submitted = st.form_submit_button("Add Task")

    if submitted:
        clean_name = task_name.strip()
        existing_names = {
            task["name"].lower()
            for task in st.session_state.tasks
        }

        if not clean_name:
            st.error("Task name is required.")
        elif clean_name.lower() in existing_names:
            st.error("This task already exists.")
        else:
            st.session_state.tasks.append(
                {
                    "id": st.session_state.next_task_id,
                    "name": clean_name,
                    "category": category,
                    "description": description.strip(),
                }
            )
            st.session_state.next_task_id += 1
            st.session_state.assignments = {}
            st.success(f"Added task: {clean_name}")

    st.subheader("Current Tasks")
    if st.session_state.tasks:
        st.dataframe(
            pd.DataFrame(st.session_state.tasks).drop(columns=["id"]),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No tasks have been added yet.")


def show_task_scoring():
    st.title("Task Scoring")
    st.caption("PB-08: Each member rates every task from 1 to 5.")

    if not st.session_state.members:
        st.warning("Add team members in Project Setup before scoring.")
        return

    if not st.session_state.tasks:
        st.warning("Add tasks in Task Brainstorming before scoring.")
        return

    st.info("Score scale: 1 = very light, 3 = medium, 5 = very heavy.")

    with st.form("score_form"):
        pending_scores = {}

        for task in st.session_state.tasks:
            with st.expander(task["name"], expanded=True):
                st.write(task["description"] or "No description.")
                pending_scores[task["id"]] = {}

                columns = st.columns(min(len(st.session_state.members), 4))
                for index, member in enumerate(st.session_state.members):
                    current_score = task_score(task["id"], member) or 3
                    with columns[index % len(columns)]:
                        pending_scores[task["id"]][member] = st.slider(
                            member,
                            min_value=1,
                            max_value=5,
                            value=int(current_score),
                            key=f"score_{task['id']}_{member}",
                        )

        submitted = st.form_submit_button("Submit Scores")

    if submitted:
        st.session_state.scores = pending_scores
        st.session_state.assignments = {}
        st.success("Scores submitted.")

    st.subheader("Task Score Summary")
    st.dataframe(score_table(), use_container_width=True, hide_index=True)


def show_assignment_result():
    st.title("Assignment Result")
    st.caption("PB-14: See each member's assigned tasks and workload score.")

    if not st.session_state.tasks:
        st.warning("Add tasks before viewing assignments.")
        return

    if not st.session_state.members:
        st.warning("Add members before viewing assignments.")
        return

    if st.button("Update Assignment Preview"):
        generate_assignment()
        st.success("Assignment preview updated.")

    if not st.session_state.assignments:
        generate_assignment()

    st.subheader("Workload Summary")
    st.dataframe(workload_rows(), use_container_width=True, hide_index=True)

    st.subheader("Assigned Tasks")
    columns = st.columns(min(len(st.session_state.members), 4))

    for index, member in enumerate(st.session_state.members):
        with columns[index % len(columns)]:
            st.markdown(f"### {member}")
            task_ids = st.session_state.assignments.get(member, [])

            if not task_ids:
                st.write("No tasks assigned.")

            for task_id in task_ids:
                task = get_task(task_id)
                if task is None:
                    continue

                st.write(
                    f"- {task['name']} "
                    f"({round(task_average(task_id) or 3, 2)} pts)"
                )


def show_dashboard():
    st.title("Dashboard")
    st.caption("PB-01: Navigation includes the main dashboard view.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Members", len(st.session_state.members))
    col2.metric("Tasks", len(st.session_state.tasks))

    scored_tasks = sum(
        1
        for task in st.session_state.tasks
        if task_score_status(task["id"])[0] == task_score_status(task["id"])[1]
    )
    col3.metric("Fully Scored Tasks", scored_tasks)

    if st.session_state.tasks:
        st.subheader("Task Scores")
        st.dataframe(
            score_table(),
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    # ======================================================
    # 自動割り振り
    # ======================================================
    st.subheader("🤖 Auto Assignment")

    if st.button("Run Auto Assignment"):
        generate_assignment()
        st.success("Assignment completed!")

    # ======================================================
    # PB17
    # ======================================================
    if st.session_state.assignments:
        workload = workload_rows()
        st.subheader("📈 PB17 Workload Graph")
        st.bar_chart(
            workload.set_index("Member")["Workload Score"]
        )

    # ======================================================
    # PB18
    # ======================================================
    st.divider()
    st.subheader("📋 PB18 Task Score Table")

    table = score_table()

    # 💡 table.empty のときに return してしまうと下のPB19が動かなくなるため、if-elseで分岐させます
    if table.empty:
        st.info("No task scores available yet.")
    else:
        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True,
        )

        discussion = table[table["Variance"] >= 1]

        if len(discussion) > 0:
            st.warning("These tasks should be discussed before assignment.")
            st.dataframe(
                discussion,
                hide_index=True,
            )
        else:
            st.success("No discussion required.")

    # ======================================================
    # PB19
    # ======================================================
    st.divider()
    st.subheader("⚖ PB19 Workload Difference")

    # 💡 ここから下の処理もしっかり「def show_dashboard():」の中にインデント(半角スペース4つ分)を入れます
    if st.session_state.assignments:
        diff = workload_difference()

        if diff <= 2:
            st.success(f"Excellent balance! Difference = {diff}")
        elif diff <= 4:
            st.warning(f"Fair balance. Difference = {diff}")
        else:
            st.error(f"Workload imbalance! Difference = {diff}")
    else:
        st.info("Run Auto Assignment first.")


# ======================================================
# アプリケーション起動・ルーティング（最下部）
# ======================================================
init_state()
selected_page = show_sidebar()

if selected_page == "Project Setup":
    show_project_setup()
elif selected_page == "Task Brainstorming":
    show_task_brainstorming()
elif selected_page == "Task Scoring":
    show_task_scoring()
elif selected_page == "Assignment Result":
    show_assignment_result()
elif selected_page == "Dashboard":
    show_dashboard()
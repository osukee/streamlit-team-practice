import statistics

import pandas as pd
import streamlit as st


def _task_average(task_id, members, scores):
    values = [
        scores.get(task_id, {}).get(member)
        for member in members
        if scores.get(task_id, {}).get(member) is not None
    ]

    if not values:
        return 0.0

    return sum(values) / len(values)


def _task_disagreement(task_id, members, scores):
    values = [
        scores.get(task_id, {}).get(member)
        for member in members
        if scores.get(task_id, {}).get(member) is not None
    ]

    if len(values) < 2:
        return 0.0

    return statistics.stdev(values)


def build_task_score_table(tasks, members, scores):
    rows = []

    for task in tasks:
        task_id = task["id"]
        submitted = sum(
            1
            for member in members
            if scores.get(task_id, {}).get(member) is not None
        )

        rows.append(
            {
                "Task": task["name"],
                "Category": task.get("category", ""),
                "Average Score": round(_task_average(task_id, members, scores), 2),
                "Disagreement": round(_task_disagreement(task_id, members, scores), 2),
                "Scores Submitted": f"{submitted}/{len(members)}",
            }
        )

    return pd.DataFrame(rows)


def build_workload_table(tasks, members, scores, assignments):
    task_names = {task["id"]: task["name"] for task in tasks}
    rows = []

    for member in members:
        task_ids = assignments.get(member, [])
        workload = sum(
            _task_average(task_id, members, scores) or 3
            for task_id in task_ids
        )

        rows.append(
            {
                "Member": member,
                "Assigned Tasks": len(task_ids),
                "Workload Score": round(workload, 2),
                "Tasks": ", ".join(
                    task_names.get(task_id, f"Task {task_id}")
                    for task_id in task_ids
                ),
            }
        )

    return pd.DataFrame(rows)


def workload_gap(workload_table):
    if workload_table.empty:
        return 0.0

    return (
        workload_table["Workload Score"].max()
        - workload_table["Workload Score"].min()
    )


def render_dashboard(tasks, members, scores, assignments):
    st.title("Dashboard")

    task_table = build_task_score_table(tasks, members, scores)
    workload_table = build_workload_table(tasks, members, scores, assignments)
    gap = workload_gap(workload_table) if assignments else 0.0

    scored_tasks = 0
    if members:
        scored_tasks = sum(
            1
            for task in tasks
            if len(scores.get(task["id"], {})) == len(members)
        )

    col1, col2, col3 = st.columns(3)
    col1.metric("Members", len(members))
    col2.metric("Tasks", len(tasks))
    col3.metric("Fully Scored Tasks", scored_tasks)

    st.subheader("Task Scores")
    if task_table.empty:
        st.info("No tasks have been added yet.")
    else:
        st.dataframe(task_table, use_container_width=True, hide_index=True)

    st.subheader("Workload")
    if not assignments:
        st.info("Generate an assignment on the Assignment Result page first.")
        return

    st.dataframe(workload_table, use_container_width=True, hide_index=True)
    st.bar_chart(workload_table.set_index("Member")["Workload Score"])

    st.subheader("Balance Gap")
    st.metric("Highest minus lowest workload", round(gap, 2))

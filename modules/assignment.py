# D：自動割り振り
"""
タスク自動割り振り機能を管理するモジュール
"""

from modules.scoring import calculate_average_scores


def assign_tasks(data):
    """
    Automatically assign tasks to members.
    """

    task_scores = calculate_average_scores(data)

    # 平均スコアが高いタスクから並べる（PB13）
    task_scores.sort(
        key=lambda x: x["average"],
        reverse=True
    )

    # メンバーごとの現在の負担
    workloads = {}

    for member in data["members"]:
        workloads[member["id"]] = 0

    assignments = []

    for task in task_scores:

        # 現在一番負担が少ないメンバー
        member_id = min(workloads, key=workloads.get)

        assignments.append({
            "task_id": task["task_id"],
            "member_id": member_id,
            "score": task["average"]
        })

        workloads[member_id] += task["average"]

    return assignments

def manual_assign_task(assignments, task_id, new_member_id):
    """
    Manually change the assigned member of a task.
    """

    for assignment in assignments:
        if assignment["task_id"] == task_id:
            assignment["member_id"] = new_member_id
            break

    return assignments


def delete_assignment(assignments, task_id):
    """
    Delete an assigned task.
    """

    assignments = [
        assignment
        for assignment in assignments
        if assignment["task_id"] != task_id
    ]

    return assignments


def add_assignment(assignments, task_id, member_id, score):
    """
    Add a new task assignment.
    """

    assignments.append({
        "task_id": task_id,
        "member_id": member_id,
        "score": score
    })

    return assignments


def update_assignment_score(assignments, task_id, new_score):
    """
    Update the score of an assigned task.
    """

    for assignment in assignments:
        if assignment["task_id"] == task_id:
            assignment["score"] = new_score
            break

    return assignments


def calculate_workloads(assignments):
    """
    Calculate total workload score for each member.
    """

    workloads = {}

    for assignment in assignments:

        member_id = assignment["member_id"]
        score = assignment["score"]

        if member_id not in workloads:
            workloads[member_id] = 0

        workloads[member_id] += score

    return workloads

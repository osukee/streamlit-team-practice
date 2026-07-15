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

# D：平均・ばらつき計算
"""
スコア計算（平均・ばらつき等）機能を管理するモジュール
"""

def calculate_average_scores(data):
    """
    Calculate the average score for each task.
    """

    scores = data["scores"]
    results = []
    task_ids = set()

    for score in scores:
        task_ids.add(score["task_id"])

    for task_id in task_ids:
        task_scores = []

        for score in scores:
            if score["task_id"] == task_id:
                task_scores.append(score["score"])

        average = sum(task_scores) / len(task_scores)

        results.append({
                    "task_id": task_id,
                    "average": average
        })

    return results
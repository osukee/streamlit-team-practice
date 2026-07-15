# D：平均・ばらつき計算
"""
スコア計算（平均・ばらつき等）機能を管理するモジュール
"""
import statistics


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

        if len(task_scores) > 1:
            disagreement = statistics.stdev(task_scores)

        else:
            disagreement = 0

        if disagreement >= 1.5:
            warning = True
        else:
            warning = False


        results.append({
                    "task_id": task_id,
                    "average": average,
                    "disagreement": disagreement,
                    "warning": warning
        })

    return results
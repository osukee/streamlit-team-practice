# B：データ保存・読み込み
"""
データ保存・読み込み機能を管理するモジュール
"""

# PB-03
def add_member(data, member_name):
    """
    メンバーを追加する関数
    """

    # 前後の空白を削除
    member_name = member_name.strip()

    # 空欄チェック
    if member_name == "":
        return data, "Member name cannot be empty."

    # 重複チェック
    for member in data["members"]:
        if member["name"] == member_name:
            return data, "This member already exists."

    # 新しいIDを作成
    new_id = len(data["members"]) + 1

    # メンバー追加
    data["members"].append({
        "id": new_id,
        "name": member_name
    })

    return data, "Member added successfully."
def get_members(data):
    """
    登録済みメンバー一覧を返す
    """
    return data["members"]
# PB-05
def add_task(data, task_name, description=""):
    """
    タスクを追加する関数
    """

    # 前後の空白を削除
    task_name = task_name.strip()
    description = description.strip()

    # 空欄チェック
    if task_name == "":
        return data, "Task name cannot be empty."

    # 重複チェック
    for task in data["tasks"]:
        if task["name"] == task_name:
            return data, "This task already exists."

    # 新しいIDを作成
    new_id = len(data["tasks"]) + 1

    # タスク追加
    data["tasks"].append({
        "id": new_id,
        "name": task_name,
        "description": description
    })

    return data, "Task added successfully."


def get_tasks(data):
    """
    登録済みタスク一覧を返す
    """
    return data["tasks"]

# PB-23
def get_sample_data():
    """
    動作確認用のサンプルデータを返す
    """
    return {
        "project_name": "Presentation Project",

        "members": [
            {"id": 1, "name": "A"},
            {"id": 2, "name": "B"},
            {"id": 3, "name": "C"},
            {"id": 4, "name": "D"},
            {"id": 5, "name": "E"}
        ],

        "tasks": [
            {
                "id": 1,
                "name": "Create slides",
                "description": "Prepare the presentation slides"
            },
            {
                "id": 2,
                "name": "Research topic",
                "description": "Collect information and references"
            },
            {
                "id": 3,
                "name": "Build Streamlit UI",
                "description": "Create the main user interface"
            },
            {
                "id": 4,
                "name": "Implement scoring logic",
                "description": "Calculate average task scores"
            },
            {
                "id": 5,
                "name": "Prepare demo",
                "description": "Create a demo scenario for the final presentation"
            }
        ],

        "scores": [
            {"task_id": 1, "member_id": 1, "score": 3},
            {"task_id": 1, "member_id": 2, "score": 4},
            {"task_id": 1, "member_id": 3, "score": 3},
            {"task_id": 1, "member_id": 4, "score": 4},
            {"task_id": 1, "member_id": 5, "score": 3},

            {"task_id": 2, "member_id": 1, "score": 4},
            {"task_id": 2, "member_id": 2, "score": 5},
            {"task_id": 2, "member_id": 3, "score": 4},
            {"task_id": 2, "member_id": 4, "score": 5},
            {"task_id": 2, "member_id": 5, "score": 4},

            {"task_id": 3, "member_id": 1, "score": 5},
            {"task_id": 3, "member_id": 2, "score": 4},
            {"task_id": 3, "member_id": 3, "score": 5},
            {"task_id": 3, "member_id": 4, "score": 4},
            {"task_id": 3, "member_id": 5, "score": 5},

            {"task_id": 4, "member_id": 1, "score": 4},
            {"task_id": 4, "member_id": 2, "score": 4},
            {"task_id": 4, "member_id": 3, "score": 3},
            {"task_id": 4, "member_id": 4, "score": 4},
            {"task_id": 4, "member_id": 5, "score": 3},

            {"task_id": 5, "member_id": 1, "score": 2},
            {"task_id": 5, "member_id": 2, "score": 3},
            {"task_id": 5, "member_id": 3, "score": 2},
            {"task_id": 5, "member_id": 4, "score": 3},
            {"task_id": 5, "member_id": 5, "score": 2}
        ]
    }

"""
グラフ・可視化機能を管理するモジュール（モジュールB、D、E 統合版）
"""
import streamlit as st
import pandas as pd
import time
import statistics

# ---------------------------------
# Page Setting
# ---------------------------------
st.set_page_config(
    page_title="FairTask Dashboard",
    page_icon="🌸",
    layout="wide"
)

# ---------------------------------
# Welcome Toast
# ---------------------------------
st.toast("🌸 Welcome to FairTask!")

# ---------------------------------
# Cute CSS
# ---------------------------------
st.markdown("""
<style>

.main {
    background-color: #FFF9FC;
}

h1 {
    color: #FF69B4;
}

[data-testid="stMetric"] {
    background-color: #FFF0F5;
    padding: 15px;
    border-radius: 15px;
    border: 2px solid #FFD6E7;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Loading Animation
# ---------------------------------
with st.spinner("Loading Dashboard..."):
    time.sleep(1)

# ---------------------------------
# Functions - Module B: Data Storage
# ---------------------------------
def add_member(data, member_name):
    """
    メンバーを追加する関数
    """
    member_name = member_name.strip()
    if member_name == "":
        return data, "Member name cannot be empty."
    for member in data["members"]:
        if member["name"] == member_name:
            return data, "This member already exists."
    new_id = len(data["members"]) + 1
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

def add_task(data, task_name, description=""):
    """
    タスクを追加する関数
    """
    task_name = task_name.strip()
    description = description.strip()
    if task_name == "":
        return data, "Task name cannot be empty."
    for task in data["tasks"]:
        if task["name"] == task_name:
            return data, "This task already exists."
    new_id = len(data["tasks"]) + 1
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
            {"id": 1, "name": "Create slides", "description": "Prepare the presentation slides"},
            {"id": 2, "name": "Research topic", "description": "Collect information and references"},
            {"id": 3, "name": "Build Streamlit UI", "description": "Create the main user interface"},
            {"id": 4, "name": "Implement scoring logic", "description": "Calculate average task scores"},
            {"id": 5, "name": "Prepare demo", "description": "Create a demo scenario for the final presentation"}
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

# ---------------------------------
# Functions - Module D: Calculations
# ---------------------------------
def calculate_average_scores(data):
    """
    Calculate the average score for each task.
    """
    scores = data["scores"]
    results = []
    task_ids = set()

    # モジュールBの「IDとタスク名」のマッピング辞書を作成
    task_map = {task["id"]: task["name"] for task in data["tasks"]}

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

        # 表示のために task_id（数値）からタスク名に変換
        task_name = task_map.get(task_id, f"Task {task_id}")

        results.append({
            "task_id": task_name,
            "average": average,
            "disagreement": disagreement
        })

    return results

# ---------------------------------
# Data Preparation (Data Binding)
# ---------------------------------

# モジュールBの関数からデータをロード
app_data = get_sample_data()

# データを元にKPIの数値を動的取得
members = len(get_members(app_data))
tasks = len(get_tasks(app_data))
fairness = 92  # フェアネス計算ロジックが組み込まれるまでは一旦固定値

# ワークロード（メンバーごとの負荷。メンバー名と連動）
workload = pd.DataFrame({
    "Member": [m["name"] for m in get_members(app_data)],
    "Workload": [10, 8, 9, 12, 7]
})

# モジュールDの計算関数を呼び出し
calculated_results = calculate_average_scores(app_data)

# モジュールEのテーブル表示に合わせた列名に変換 (DataFrame化)
task_table = pd.DataFrame(calculated_results).rename(columns={
    "task_id": "Task",
    "average": "Average Score",
    "disagreement": "Variance"
})

# ---------------------------------
# Title
# ---------------------------------
st.title("🌸 FairTask Dashboard")
st.caption("Making Group Work Fair and Balanced")

st.markdown("### ✨ Dashboard Summary")
st.write(
    "This dashboard helps teams visualize workload balance "
    "and identify tasks that need discussion."
)

st.divider()

# ---------------------------------
# KPI Cards
# ---------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Members", members)

with col2:
    st.metric("📋 Tasks", tasks)

with col3:
    st.metric("⚖ Fairness", f"{fairness}%")

# ---------------------------------
# Fairness Alert
# ---------------------------------
if fairness >= 90:
    st.success("🎉 Excellent! Everyone's workload is very balanced.")
    st.balloons()

elif fairness >= 75:
    st.warning("😊 Good! The workload is almost balanced.")

else:
    st.error("⚠ Workload is unbalanced. Consider reassigning tasks.")

st.divider()

# ---------------------------------
# Team Overview
# ---------------------------------
st.markdown("### 📈 Team Overview")

highest = workload.loc[workload["Workload"].idxmax()]

st.info(
    f"🏆 Highest Workload: **{highest['Member']}** "
    f"({highest['Workload']} points)"
)

# ---------------------------------
# Workload Graph
# ---------------------------------
st.subheader("📊 Workload Distribution")

st.bar_chart(
    workload.set_index("Member")
)

st.divider()

# ---------------------------------
# Task Summary
# ---------------------------------
st.subheader("📋 Task Summary")

st.dataframe(
    task_table,
    use_container_width=True
)

# ---------------------------------
# Tasks to Discuss
# ---------------------------------
st.subheader("⚠ Tasks to Discuss")

discussion = task_table[task_table["Variance"] >= 1.0]

if discussion.empty:
    st.success("No major disagreements between members.")

else:
    for _, row in discussion.iterrows():
        st.warning(
            f"**{row['Task']}**\n\n"
            f"Variance: **{row['Variance']:.2f}**\n\n"
            "Members have different opinions. "
            "Please discuss before assigning this task."
        )

st.divider()

# ---------------------------------
# FairTask Assistant
# ---------------------------------
st.subheader("🤖 FairTask Assistant")

st.success("🎉 Great! This dashboard currently uses sample data from Module B & D.")
st.info("📁 CSV integration will be added in Sprint 2.")

st.divider()
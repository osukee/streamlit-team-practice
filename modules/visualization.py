import streamlit as st
import pandas as pd
import time
import statistics
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# ===========================================================================
# 共有データモデル（データクラス定義）
# ===========================================================================
@dataclass
class Project:
    """プロジェクト（グループワーク単位）。PB-02 で作成する。"""
    name: str
    description: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M"))

@dataclass
class Member:
    """グループメンバー。PB-03 で登録、PB-04 で working_hours を追加予定。"""
    id: str
    name: str
    available_hours: Optional[float] = None  # PB-04（任意項目）

@dataclass
class Task:
    """タスク。PB-05 で登録、PB-06 で category を追加予定。"""
    id: str
    title: str
    category: Optional[str] = None  # PB-06（任意項目）

# ---------------------------------
# session_state の初期化
# ---------------------------------
_DEFAULTS = {
    "project": None,     # Project | None
    "members": [],       # list[Member]
    "tasks": [],         # list[Task]
    "scores": {},        # dict[task_id, dict[member_id, int]]
    "assignment": {},    # dict[member_id, list[task_id]]
}

def init_session_state() -> None:
    """アプリ全体で使う session_state を初期化する。各ページの先頭で必ず呼ぶこと。"""
    for key, default_value in _DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default_value.copy() if isinstance(default_value, (dict, list)) else default_value
    if "is_cleared" not in st.session_state:
        st.session_state["is_cleared"] = False

# ===========================================================================
# サンプルデータ投入関数（動作確認・提出時の初期表示用）
# ===========================================================================
def load_sample_data():
    """データモデルの構造に合わせて検証用のサンプルデータを注入する"""
    st.session_state["project"] = Project(name="Presentation Project", description="Sample project for demo")
    
    st.session_state["members"] = [
        Member(id="m1", name="A"),
        Member(id="m2", name="B"),
        Member(id="m3", name="C"),
        Member(id="m4", name="D"),
        Member(id="m5", name="E"),
    ]
    
    st.session_state["tasks"] = [
        Task(id="t1", title="Create slides"),
        Task(id="t2", title="Research topic"),
        Task(id="t3", title="Build Streamlit UI"),
        Task(id="t4", title="Implement scoring logic"),
        Task(id="t5", title="Prepare demo"),
    ]
    
    st.session_state["scores"] = {
        "t1": {"m1": 3, "m2": 4, "m3": 3, "m4": 4, "m5": 3},
        "t2": {"m1": 4, "m2": 5, "m3": 4, "m4": 5, "m5": 4},
        "t3": {"m1": 5, "m2": 4, "m3": 5, "m4": 4, "m5": 5},
        "t4": {"m1": 4, "m2": 4, "m3": 3, "m4": 4, "m5": 3},
        "t5": {"m1": 2, "m2": 3, "m3": 2, "m4": 3, "m5": 2},
    }
    
    st.session_state["assignment"] = {
        "m1": ["t1", "t5"],  # 合計平均負荷: 3.4 + 2.4 = 5.8
        "m2": ["t2"],        # 合計平均負荷: 4.4
        "m3": ["t3"],        # 合計平均負荷: 4.6
        "m4": ["t4"],        # 合計平均負荷: 3.6
        "m5": [],            # 合計平均負荷: 0.0
    }
    st.session_state["is_cleared"] = False

# ===========================================================================
# 共通計算ロジック（データモデル準拠）
# ===========================================================================
def calculate_task_metrics():
    """各タスクの平均スコアとばらつきを計算する"""
    scores_dict = st.session_state.get("scores", {})
    tasks_list = st.session_state.get("tasks", [])
    
    task_map = {t.id: t.title for t in tasks_list}
    results = []
    
    for task_id, member_scores in scores_dict.items():
        score_values = list(member_scores.values())
        if not score_values:
            continue
            
        average = sum(score_values) / len(score_values)
        disagreement = statistics.stdev(score_values) if len(score_values) > 1 else 0.0
        
        task_title = task_map.get(task_id, f"Task {task_id}")
        
        results.append({
            "task_id": task_id,
            "Task": task_title,
            "Average Score": average,
            "Variance": disagreement
        })
        
    return pd.DataFrame(results)

def calculate_member_workloads(task_metrics_df):
    """
    【PB-17 負担の定義に関する発表時想定問答用メモ】
    ★質問：「負担って作業時間じゃないの？」
    👉回答：「現時点ではタスク難易度スコアの合計を負担量として扱っています。今後PB-04の作業可能時間が追加された場合は、[時間 × 難易度] の形でロジックを簡単に拡張できるよう設計しています」
    """
    members_list = st.session_state.get("members", [])
    assignment_dict = st.session_state.get("assignment", {})
    
    if not task_metrics_df.empty:
        task_score_map = dict(zip(task_metrics_df["task_id"], task_metrics_df["Average Score"]))
    else:
        task_score_map = {}
        
    workload_data = []
    for m in members_list:
        assigned_task_ids = assignment_dict.get(m.id, [])
        total_workload = sum(task_score_map.get(tid, 0.0) for tid in assigned_task_ids)
        
        workload_data.append({
            "Member": m.name,
            "Workload": total_workload
        })
        
    return pd.DataFrame(workload_data)

# ===========================================================================
# Streamlit アプリケーション メイン処理
# ===========================================================================

# 1. ページ初期設定
st.set_page_config(
    page_title="FairTask Dashboard",
    page_icon="🌸",
    layout="wide"
)

# 2. セッションステート初期化
init_session_state()

# 初回起動時（明示的にクリアされていない場合）のみサンプルデータを自動ロード
if not st.session_state["members"] and not st.session_state["is_cleared"]:
    load_sample_data()

# 可愛いCSSスタイル
st.markdown("""
<style>
.main { background-color: #FFF9FC; }
h1 { color: #FF69B4; }
[data-testid="stMetric"] {
    background-color: #FFF0F5;
    padding: 15px;
    border-radius: 15px;
    border: 2px solid #FFD6E7;
}
</style>
""", unsafe_allow_html=True)

# タイトル表示
st.title("🌸 FairTask Dashboard")
st.caption("Making Group Work Fair and Balanced")

# ---------------------------------
# データが空の場合の表示（リセット後など）
# ---------------------------------
if not st.session_state["members"]:
    st.info("現在、登録されているメンバーやタスクのデータがありません。")
    if st.button("🚀 デモ用のサンプルデータを読み込む"):
        load_sample_data()
        st.rerun()

# ---------------------------------
# データが存在する場合のダッシュボード描画
# ---------------------------------
else:
    # 事前データ計算
    task_table_df = calculate_task_metrics()
    workload_df = calculate_member_workloads(task_table_df)
    
    total_members = len(st.session_state["members"])
    total_tasks = len(st.session_state["tasks"])
    
    if not workload_df.empty:
        max_workload = workload_df["Workload"].max()
        min_workload = workload_df["Workload"].min()
        workload_difference = max_workload - min_workload
    else:
        workload_difference = 0.0

    # サマリー指標（KPI）の表示
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👥 Members", total_members)
    with col2:
        st.metric("📋 Tasks", total_tasks)
    with col3:
        st.metric("⚖ Workload Diff (負担差)", f"{workload_difference:.2f} pts")

    st.divider()

    # =======================================================================
    # PB-19 負担差表示
    # =======================================================================
    st.markdown("### ⚖ 負担差評価 (PB-19)")
    
    if workload_difference <= 2.0:
        st.success(f"🎉 負担差は **{workload_difference:.2f}** ポイントです。全員のワークロードが非常に均等です。")
    elif workload_difference <= 4.5:
        st.warning(f"😊 概ね良好です。負担差は **{workload_difference:.2f}** ポイントです。わずかに偏りがあります。")
    else:
        st.error(f"⚠ 警告: ワークロードが不均等です！ 負担差が **{workload_difference:.2f}** ポイントに達しています。タスクの再配分を検討してください。")

    st.divider()

    # =======================================================================
    # PB-17 負担グラフ
    # =======================================================================
    st.markdown("### 📈 チームの負荷分布 (PB-17)")
    
    highest_member = workload_df.loc[workload_df["Workload"].idxmax()]
    lowest_member = workload_df.loc[workload_df["Workload"].idxmin()]
    
    col_chart, col_info = st.columns([2, 1])
    
    with col_chart:
        st.subheader("📊 メンバー別 負担グラフ")
        st.bar_chart(workload_df.set_index("Member"))
        
    with col_info:
        st.subheader("🔍 負荷のサマリー")
        st.info(f"🔺 **最大負担者**: {highest_member['Member']} ({highest_member['Workload']:.2f} pts)")
        st.info(f"🔻 **最小負担者**: {lowest_member['Member']} ({lowest_member['Workload']:.2f} pts)")
        st.caption("※ 現在の負担ポイントは、割り当てられたタスクの『平均難易度スコア』の合計値で算出されています。")

    st.divider()

    # =======================================================================
    # PB-18 タスクスコア表
    # =======================================================================
    st.markdown("### 📋 タスクスコア表 (PB-18)")
    st.write("各タスクの平均スコア（難易度）と、メンバー間の意見のばらつき（不一致度）の一覧です。")
    
    if not task_table_df.empty:
        display_table = task_table_df[["Task", "Average Score", "Variance"]]
        st.dataframe(display_table, use_container_width=True)
    else:
        st.caption("評価スコアがまだ入力されていません。")

    # 議論が必要なタスク (ばらつきが大きいタスク) のアラート表示
    st.subheader("⚠ 要話し合いタスク")
    if not task_table_df.empty:
        discussion_tasks = task_table_df[task_table_df["Variance"] >= 1.0]
        if discussion_tasks.empty:
            st.success("メンバー間の認識のズレが少ないため、スムーズに分配可能です。")
        else:
            for _, row in discussion_tasks.iterrows():
                st.warning(
                    f"**【{row['Task']}】** (不一致度 Variance: **{row['Variance']:.2f}**)\n\n"
                    f"このタスクは難易度の見積もりに個人差があります。割り振る前に認識を合わせるための話し合いを推奨します。"
                )

    st.divider()
    
    # ---------------------------------
    # 管理用：完全リセットボタン（データをクリアして空の状態にする）
    # ---------------------------------
    if st.button("🔄 データを完全にクリア（初期状態へ戻す）"):
        # セッション状態をデフォルト値で上書きし、クリアフラグを立てる
        for key in _DEFAULTS.keys():
            st.session_state[key] = _DEFAULTS[key].copy() if isinstance(_DEFAULTS[key], (dict, list)) else _DEFAULTS[key]
        st.session_state["is_cleared"] = True
        st.rerun()
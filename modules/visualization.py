# E：グラフ
"""
グラフ・可視化機能を管理するモジュール
"""
import streamlit as st
import pandas as pd
import time

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
# Sample Data (Temporary)
# ---------------------------------

members = 5
tasks = 12
fairness = 92

workload = pd.DataFrame({
    "Member": ["Alice", "Bob", "Chris", "David", "Emma"],
    "Workload": [10, 8, 9, 12, 7]
})

task_table = pd.DataFrame({
    "Task": ["Backend", "UI Design", "Presentation", "Testing"],
    "Average Score": [4.8, 4.5, 3.2, 2.4],
    "Variance": [1.1, 0.5, 0.3, 0.8]
})

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
            f"Variance: **{row['Variance']}**\n\n"
            "Members have different opinions. "
            "Please discuss before assigning this task."
        )

st.divider()

# ---------------------------------
# FairTask Assistant
# ---------------------------------

st.subheader("🤖 FairTask Assistant")

st.success("🎉 Great! This dashboard currently uses sample data.")

st.info("📁 CSV integration will be added in Sprint 2.")

st.divider()

# ---------------------------------
# Celebrate
# ---------------------------------

st.markdown("### 🎉 Celebrate!")

if st.button("❄ Celebrate Teamwork"):
    st.snow()

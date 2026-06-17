import streamlit as st
import pandas as pd
st.title("My First Deployed Streamlit App")
st.write("This app was created in VS Code and deployed from GitHub.")
data = {
"Name": ["Alice", "Bob", "Charlie"],
"Score": [85, 92, 78],
}
df = pd.DataFrame(data)
st.subheader("Student Scores")
st.dataframe(df)
st.bar_chart(df.set_index("Name"))

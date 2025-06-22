
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mini DFT Analyzer", layout="wide")

st.markdown("## 🔧 DFT Analyzer")
st.caption("A compact dashboard to explore Design for Test (DFT) results.")

conn = sqlite3.connect("dft_data.db")
df = pd.read_sql_query("SELECT * FROM dft_results", conn)

with st.sidebar:
    st.header("🔍 Filters")
    scan_chain_filter = st.multiselect("Scan Chains:", df["scan_chain"].unique(), default=df["scan_chain"].unique())
    min_pass_rate = st.slider("Minimum Pass Rate (%)", 0, 100, 70)


df["timestamp"] = pd.to_datetime(df["timestamp"])
filtered_df = df[(df["scan_chain"].isin(scan_chain_filter)) & (df["pass_rate"] >= min_pass_rate)]

# Compact display: Table + Metrics
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### 📋 Filtered Results")
    st.dataframe(filtered_df, height=300, use_container_width=True)

with col2:
    st.markdown("#### 📊 Key Metrics")
    st.metric("Avg Pass Rate", f"{filtered_df['pass_rate'].mean():.2f}%")
    st.metric("Avg Test Time", f"{filtered_df['test_time_ms'].mean():.0f} ms")

# 3 Compact charts side-by-side
col3, col4, col5 = st.columns(3)

with col3:
    avg_pass = filtered_df.groupby("scan_chain")["pass_rate"].mean().reset_index()
    fig1 = px.bar(avg_pass, x="scan_chain", y="pass_rate", height=250)
    st.plotly_chart(fig1, use_container_width=True)

with col4:
    scan_counts = filtered_df["scan_chain"].value_counts().reset_index()
    scan_counts.columns = ["scan_chain", "count"]
    fig2 = px.pie(scan_counts, names="scan_chain", values="count", height=250)
    st.plotly_chart(fig2, use_container_width=True)

with col5:
    fig3 = px.line(filtered_df.sort_values("timestamp"), x="timestamp", y="pass_rate", color="scan_chain", markers=True, height=250)
    st.plotly_chart(fig3, use_container_width=True)

conn.close()

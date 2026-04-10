# app.py
import streamlit as st
import pandas as pd
from data_generator import generate_mock_traffic
from predictor import analyze_traffic
from config import APP_TITLE, DEFAULT_ROWS

# Page Configuration
st.set_page_config(page_title=APP_TITLE, layout="wide")
st.title(f"🛡️ {APP_TITLE}")

st.markdown("This dashboard uses a Hugging Face Machine Learning model to detect network anomalies in real-time.")

# Sidebar Controls
st.sidebar.header("Control Panel")
num_packets = st.sidebar.slider("Number of Packets to Simulate", 5, 100, DEFAULT_ROWS)

if st.sidebar.button("Run Traffic Analysis"):
    with st.spinner("Generating traffic and analyzing with AI..."):
        # 1. Generate Data
        raw_data = generate_mock_traffic(num_rows=num_packets)
        
        # 2. Predict Anomalies
        results_df = analyze_traffic(raw_data)
        
        # --- DASHBOARD UI ---
        
        # Metrics Row
        total_packets = len(results_df)
        attacks = len(results_df[results_df["Is_Anomaly"] == 1])
        safe = total_packets - attacks
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Packets Analyzed", total_packets)
        col2.metric("Normal Traffic ✅", safe)
        col3.metric("Anomalies Detected 🚨", attacks, delta_color="inverse")
        
        st.divider()
        
        # Alert Table
        st.subheader("Real-Time Packet Log")
        
        # We display the IPs, the status, and the first 3 features to keep it clean
        display_columns = ["Source_IP", "Dest_IP", "Status", "Feature_1", "Feature_2", "Feature_3"]
        st.dataframe(results_df[display_columns], use_container_width=True)
        
        # Simple Bar Chart Visualization
        st.subheader("Traffic Distribution")
        chart_data = pd.DataFrame(
            {"Count": [safe, attacks]}, 
            index=["Safe", "Anomalous"]
        )
        st.bar_chart(chart_data)

else:
    st.info("👈 Click 'Run Traffic Analysis' in the sidebar to start.")
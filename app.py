import streamlit as st
import pandas as pd
from util.helpers import detect_threats

st.title("🔍 Log Analyzer")
st.write("Upload a `.txt` or `.log` file containing log entries.")

# Accept txt and log files
uploaded_file = st.file_uploader("Choose a log file", type=["txt", "log"])

if uploaded_file is not None:
    try:
        # Read file line by line
        log_lines = uploaded_file.read().decode("utf-8").splitlines()
        st.write("### Raw Log Preview")
        st.code("\n".join(log_lines[:10]), language='text')  # Preview top 10 lines

        # Convert to DataFrame with one column: 'message'
        df = pd.DataFrame(log_lines, columns=["message"])

        # Detect threats
        alerts = detect_threats(df)

        st.write("## 🚨 Detected Alerts")
        if alerts:
            st.dataframe(pd.DataFrame(alerts))
        else:
            st.success("No threats detected!")
    except Exception as e:
        st.error(f"Error reading file: {e}")

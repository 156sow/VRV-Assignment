"""
Web Server Log Analyzer
A tool for analyzing web server logs to monitor traffic patterns, detect security threats. 
Generate visual insights.

Author: Sepuri Sai Sowmya
Date: 06/12/2024
"""


import os
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils import LogAnalysis, DataVisualization

def main():
    st.title("Log File Analysis Tool")
    st.write("Upload a log file to analyze web traffic and detect potential security threats.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a log file", type=["log"])

    if uploaded_file is not None:
        # Ensure 'temp' directory exists
        os.makedirs("temp", exist_ok=True)

        # Save uploaded file temporarily
        file_path = f"temp/{uploaded_file.name}"
        with open(file_path, "wb") as file:
            file.write(uploaded_file.read())

        # Validate log file
        if not LogAnalysis.validate_log_format(file_path):
            st.error("The log file format is invalid. Please upload a valid log file.")
            return

        # Parse log file into a DataFrame
        log_data = LogAnalysis.parse_logs_to_dataframe(file_path)

        # Visualization Buttons
        st.subheader("Visualization")
        col1, col2, col3, col4 = st.columns(4)  # Arrange buttons in a row
        with col1:
            if st.button("Requests Over Time"):
                DataVisualization.plot_requests_over_time(log_data)
        with col2:
            if st.button("Status Code Distribution"):
                DataVisualization.plot_status_code_distribution(log_data)
        with col3:
            if st.button("Failed Login Attempts"):
                DataVisualization.plot_failed_login_heatmap(log_data)
        with col4:
            if st.button("Endpoint Access"):
                DataVisualization.plot_endpoint_access_distribution(log_data)

        # Display raw data
        st.subheader("Log File Data")
        st.dataframe(log_data)

        # Analysis: Requests per IP Address
        st.subheader("Requests per IP Address")
        ip_requests = LogAnalysis.count_requests_by_ip(log_data)
        st.table(ip_requests)

        # Analysis: Most Frequently Accessed Endpoint
        st.subheader("Most Frequently Accessed Endpoint")
        top_endpoint, access_count = LogAnalysis.get_top_endpoint(log_data)
        st.write(f"**Endpoint:** {top_endpoint} (Accessed {access_count} times)")

        # Analysis: Suspicious Activity Detection
        st.subheader("Suspicious Activity Detected")
        suspicious_ips = LogAnalysis.find_suspicious_ips(log_data)
        if not suspicious_ips.empty:
            st.table(suspicious_ips)
        else:
            st.write("No suspicious activity detected.")

if __name__ == "__main__":
    main()

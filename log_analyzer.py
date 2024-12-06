"""
Web Server Log Analyzer
Analyzes web server logs to track traffic patterns and detect security threats.
Generate reports in CSV format.
Author: Sepuri Sai Sowmya
Date: 06/12/2024
"""


import re
from collections import defaultdict
import pandas as pd

# Function to parse the log file
def parse_log_file(file_path):
    log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).+?"(?P<method>\w+) (?P<endpoint>/\S+).*?" (?P<status>\d+)')
    failed_login_message = "Invalid credentials"
    
    log_data = []

    with open(file_path, 'r') as log_file:
        for line in log_file:
            match = log_pattern.search(line)
            if match:
                ip = match.group("ip")
                endpoint = match.group("endpoint")
                status = match.group("status")
                
                failed_login = int(status == "401" or failed_login_message in line)
                log_data.append({"IP Address": ip, "Endpoint": endpoint, "Status": status, "Failed Login": failed_login})
    
    return pd.DataFrame(log_data)

# Function to analyze requests per IP
def analyze_requests_per_ip(log_df):
    return log_df.groupby("IP Address").size().reset_index(name="Request Count").sort_values(by="Request Count", ascending=False)

# Function to analyze endpoints
def analyze_endpoints(log_df):
    return log_df.groupby("Endpoint").size().reset_index(name="Access Count").sort_values(by="Access Count", ascending=False)

# Function to detect suspicious activity
def detect_suspicious_activity(log_df, threshold=10):
    failed_logins = log_df.groupby("IP Address")["Failed Login"].sum().reset_index()
    return failed_logins[failed_logins["Failed Login"] > threshold]

# Function to print and save consolidated results
def save_and_print_results(ip_requests, endpoint_requests, flagged_ips, most_accessed, file_name="results.csv"):
    with open(file_name, "w") as file:
        # Print and save Requests per IP
        print("IP Requests:")
        print("IP Address, Request Count")
        file.write("IP Requests:\n")
        file.write("IP Address, Request Count\n")
        for _, row in ip_requests.iterrows():
            print(f"{row['IP Address']}, {row['Request Count']}")
            file.write(f"{row['IP Address']}, {row['Request Count']}\n")
        print("\n")
        file.write("\n")

        # Print and save Most Frequently Accessed Endpoint
        print("Most Frequently Accessed Endpoint:")
        print(f"{most_accessed['Endpoint']} (Accessed {most_accessed['Access Count']} times)\n")
        file.write("Most Frequently Accessed Endpoint:\n")
        file.write(f"{most_accessed['Endpoint']} (Accessed {most_accessed['Access Count']} times)\n\n")

        # Print and save Suspicious Activity
        print("Suspicious Activity:")
        file.write("Suspicious Activity:\n")
        if not flagged_ips.empty:
            print("IP Address, Failed Login Count")
            file.write("IP Address, Failed Login Count\n")
            for _, row in flagged_ips.iterrows():
                print(f"{row['IP Address']}, {row['Failed Login']}")
                file.write(f"{row['IP Address']}, {row['Failed Login']}\n")
        else:
            print("No suspicious activity detected.")
            file.write("No suspicious activity detected.\n")
        print("\n")
        file.write("\n")

# Main function
def analyze_log(file_path, failed_attempt_threshold=10):
    # Parse the log file
    log_df = parse_log_file(file_path)
    
    # Perform analysis
    ip_requests = analyze_requests_per_ip(log_df)
    endpoint_requests = analyze_endpoints(log_df)
    flagged_ips = detect_suspicious_activity(log_df, failed_attempt_threshold)
    most_accessed = endpoint_requests.iloc[0]
    
    # Save and print results
    save_and_print_results(ip_requests, endpoint_requests, flagged_ips, most_accessed)

# Run the script
if __name__ == "__main__":
    log_file_path = "sample.log"
    analyze_log(log_file_path)

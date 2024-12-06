import re
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

class LogAnalysis:
    """
    A class for log file validation, parsing, and analysis.
    """
    FAILED_LOGIN_THRESHOLD = 10  # Threshold for detecting suspicious login attempts

    @staticmethod
    def validate_log_format(file_path):
        """
        Validates the structure of a log file based on a predefined pattern.

        Args:
            file_path (str): Path to the log file.

        Returns:
            bool: True if the log file is valid, False otherwise.
        """
        log_regex = (
            r'^(?P<ip>\d+\.\d+\.\d+\.\d+) '                         # IP address
            r'- - '
            r'\[(?P<timestamp>.*?)\] '                              # Timestamp
            r'"(?P<method>[A-Z]+) (?P<endpoint>/[^ ]*) [^"]+" '     # HTTP method and endpoint
            r'(?P<status>\d+) '                                     # HTTP status code
            r'(?P<size>\d+)(?: "(?P<message>.*?)")?$'               # Response size and optional message
        )
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if not re.match(log_regex, line.strip()):
                        return False
            return True
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return False

    @staticmethod
    def parse_logs_to_dataframe(file_path):
        """
        Converts a valid log file into a pandas DataFrame.

        Args:
            file_path (str): Path to the log file.

        Returns:
            pandas.DataFrame: Parsed log data.
        """
        log_entries = []
        log_regex = (
            r'^(?P<ip>\d+\.\d+\.\d+\.\d+) '  # IP address
            r'- - '
            r'\[(?P<timestamp>.*?)\] '       # Timestamp
            r'"(?P<method>[A-Z]+) (?P<endpoint>/[^ ]*) [^"]+" '  # Method and endpoint
            r'(?P<status>\d+) '              # HTTP status code
            r'(?P<size>\d+)(?: "(?P<message>.*?)")?$'  # Response size and optional message
        )

        with open(file_path, 'r') as file:
            for line in file:
                match = re.match(log_regex, line.strip())
                if match:
                    log_entries.append(match.groupdict())

        return pd.DataFrame(log_entries)

    @staticmethod
    def count_requests_by_ip(dataframe):
        """
        Counts requests made by each IP address.

        Args:
            dataframe (pandas.DataFrame): DataFrame containing parsed log data.

        Returns:
            pandas.DataFrame: DataFrame showing IPs and their request counts.
        """
        ip_request_counts = dataframe['ip'].value_counts().reset_index()
        ip_request_counts.columns = ['IP Address', 'Request Count']
        return ip_request_counts

    @staticmethod
    def get_top_endpoint(dataframe):
        """
        Finds the most accessed endpoint and its access count.

        Args:
            dataframe (pandas.DataFrame): DataFrame containing parsed log data.

        Returns:
            tuple: (Endpoint, access count) of the most accessed endpoint.
        """
        endpoint_counts = dataframe['endpoint'].value_counts()
        return endpoint_counts.idxmax(), endpoint_counts.max()

    @staticmethod
    def find_suspicious_ips(dataframe):
        """
        Identifies suspicious IP addresses based on failed login attempts.

        Args:
            dataframe (pandas.DataFrame): DataFrame containing parsed log data.

        Returns:
            pandas.DataFrame: DataFrame of IPs and failed login counts exceeding the threshold.
        """
        failed_logins = dataframe[dataframe['status'] == '401']
        suspicious_ip_counts = failed_logins['ip'].value_counts()
        suspicious_ips = suspicious_ip_counts[suspicious_ip_counts > LogAnalysis.FAILED_LOGIN_THRESHOLD].reset_index()
        suspicious_ips.columns = ['IP Address', 'Failed Login Count']
        return suspicious_ips


class DataVisualization:
    """
    A class for visualizing log data.
    """

    @staticmethod
    def plot_requests_over_time(dataframe):
        """Visualizes request counts over time."""
        try:
            dataframe['timestamp'] = pd.to_datetime(dataframe['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')
        except Exception as e:
            st.error(f"Error parsing timestamps: {e}")
            return

        requests_per_minute = dataframe.set_index('timestamp').resample('T').size()

        plt.figure(figsize=(10, 6))
        requests_per_minute.plot()
        plt.title("Requests Over Time")
        plt.xlabel("Time")
        plt.ylabel("Number of Requests")
        plt.grid(True)
        st.pyplot(plt)

    @staticmethod
    def plot_status_code_distribution(dataframe):
        """Visualizes the distribution of HTTP status codes."""
        status_counts = dataframe['status'].value_counts()

        plt.figure(figsize=(8, 5))
        status_counts.plot(kind='bar', color='skyblue')
        plt.title("HTTP Status Code Distribution")
        plt.xlabel("HTTP Status Code")
        plt.ylabel("Count")
        plt.grid(True)
        st.pyplot(plt)

    @staticmethod
    def plot_failed_login_heatmap(dataframe):
        """Visualizes failed login attempts as a heatmap."""
        try:
            dataframe['timestamp'] = pd.to_datetime(dataframe['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')
        except Exception as e:
            st.error(f"Error parsing timestamps: {e}")
            return

        failed_logins = dataframe[dataframe['status'] == '401']

        if failed_logins.empty:
            st.write("No failed login attempts detected.")
            return

        failed_logins['hour'] = failed_logins['timestamp'].dt.hour
        failed_logins['day'] = failed_logins['timestamp'].dt.strftime('%A')

        heatmap_data = failed_logins.pivot_table(index='day', columns='hour', aggfunc='size', fill_value=0)

        plt.figure(figsize=(12, 6))
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='coolwarm')
        plt.title("Failed Login Attempts by Hour and Day")
        plt.xlabel("Hour of Day")
        plt.ylabel("Day of Week")
        st.pyplot(plt)

    @staticmethod
    def plot_endpoint_access_distribution(dataframe):
        """Visualizes the access frequency of endpoints."""
        endpoint_counts = dataframe['endpoint'].value_counts()

        plt.figure(figsize=(10, 6))
        endpoint_counts.plot(kind='bar', color='purple')
        plt.title("Endpoint Access Frequency")
        plt.xlabel("Endpoints")
        plt.ylabel("Access Count")
        plt.grid(True)
        st.pyplot(plt)

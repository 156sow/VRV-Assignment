# VRV Assignment

This repository provides a complete log analysis solution, featuring a Jupyter Notebook for step-by-step exploration, a standalone Python script for automated processing, and a Streamlit-based web app for interactive visualization of log data.

---

## Project Structure

### Root Directory
- **`log_analysis.ipynb`**: An interactive Jupyter Notebook that demonstrates log file analysis with detailed instructions and visualizations, ideal for understanding and exploring log data.
- **`log_analysis.py`**: A Python script designed for automated log file analysis, generating insights such as request counts, accessed endpoints, and suspicious activities, saved in a CSV format.
- **`log_analysis_results.csv`**: Output CSV file containing processed log data, including request statistics, endpoint access counts, and detected suspicious activities.
- **`sample.log`**: A sample log file with 10,000 entries, used for testing and demonstrating the solution.

### `Streamlit_APP` Directory
- **`app.py`**: The main script for the Streamlit web app, which allows users to upload and analyze log files interactively with real-time visualizations.
- **`utils.py`**: A collection of helper functions used by the Streamlit app for processing log data and generating insights in visual formats like charts and graphs.
- **`temp/`**: A temporary directory for storing uploaded log files during analysis, including a placeholder `sample.log` for testing.

---

## Usage Guide

### 1. Running the Python Script
1. Execute the `log_analysis.py` script using the command:
   ```bash
   python log_analysis.py
   ```
2. The script processes the log file and generates insights, saving them in a CSV file named `log_analysis_results.csv`.
3. Review the CSV file to explore key findings, including request counts and suspicious activity detections.

### 2. Launching the Streamlit App
1. Navigate to the `Streamlit_APP` directory.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Streamlit app with:
   ```bash
   streamlit run app.py
   ```
4. Use the web app to upload log files and view interactive visualizations, such as request distributions and failed login patterns.

---

## Features

### 1. Jupyter Notebook for Log Analysis
The `log_analysis.ipynb` notebook offers a hands-on approach to log analysis, enabling tasks like:
- **IP Address Request Counts**: Analyze the number of requests per IP address.
- **Frequent Endpoint Access**: Identify the most accessed endpoints.
- **Suspicious Activity Detection**: Spot repeated failed login attempts from specific IPs.

### 2. Streamlit Visualization
The Streamlit app provides real-time visualizations, including:
- **Requests per IP Address**: Bar charts showing request counts by IP.
- **Most Accessed Endpoints**: A summary of the most visited endpoints.
- **Failed Login Heatmap**: Heatmaps displaying failed login attempts by time.
- **Requests Over Time**: Line charts tracking request trends.

These visualizations help uncover patterns, trends, and potential security threats.

---

## Prerequisites
- **Python 3.8+**
- Required libraries: 
  - **Pandas**: For data manipulation.
  - **Streamlit**: For the interactive web app.
  - **Matplotlib & Seaborn**: For visualizations.

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Sample Input Format
Example log entries expected by the tools:

```plaintext
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
```

---

## Sample Output

### Python Script Output
- **Request Counts per IP Address**:
  ```plaintext
   IP Address      Request Count
  203.0.113.5             15
  198.51.100.23           8
  ```
- **Most Accessed Endpoint**:
  ```plaintext
  Endpoint: /login (Accessed 13 times)
  ```
- **Suspicious Activity Detected**:
  ```plaintext
   IP Address      Failed Login Count
  203.0.113.5             15
  ```

### Streamlit Visualizations
- **Requests Over Time**: A line chart displaying request trends over time.
![image](https://github.com/user-attachments/assets/5b619efb-9dde-4ba6-95ae-ee79359c6078)
- **Status Code Distribution**: A bar chart showing the frequency of HTTP status codes.
![image](https://github.com/user-attachments/assets/c8547010-cad4-48bd-a11a-15c13649cdd1)
- **Failed Login Heatmap**: A heatmap visualizing failed login attempts by hour and day.
![image](https://github.com/user-attachments/assets/89dc86d8-c179-454f-be57-17fc4c29c945)
- **Endpoint Access Frequency**: A bar chart highlighting the most accessed endpoints.
![image](https://github.com/user-attachments/assets/d36c94d2-2658-4ef3-b04a-be7d4f44e8ab)

These features collectively provide a robust framework for analyzing and visualizing log data.



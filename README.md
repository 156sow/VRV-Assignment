# Web Server Log Analyzer

A powerful tool for analyzing web server logs to track traffic patterns, detect security threats, and visualize critical insights. This project leverages Python, pandas, Matplotlib, Seaborn, and Streamlit to deliver robust log analysis and visualizations.

## Features

- **Log Validation**: Ensure uploaded log files match the required format.
- **Traffic Analysis**: Visualize requests over time, HTTP status code distributions, and endpoint usage.
- **Suspicious Activity Detection**: Detect potential brute force attacks based on failed login attempts.
- **Interactive Visualizations**: Explore data using rich and intuitive Streamlit-powered dashboards.
- **CSV Report Generation**: Summarize analysis in downloadable CSV files.
Here’s an explanation of the project structure and directories for your **Web Server Log Analyzer**:

---

## Project Structure

```
web-server-log-analyzer/
├── log_analyzer.py          # Standalone python script that automates log files analysis.
├── Web_App
|  ├── app.py                # Main Streamlit application file
|  ├── utils/                # Utility modules for log analysis and visualization
|  │   ├── log_analyzer.py   # Functions for log validation, parsing, and analysis
|  │   ├── visualizations.py # Functions for generating visualizations
|  │
|  ├── temp/                 # Temporary directory for uploaded log files
│
├── requirements.txt      # List of required Python packages
├── 
└── LICENSE               # License file (if applicable)
```

### **Explanation of Directories and Files**
#### 1. **`log_analyzer.py`**
   - This script processes log data and generates insights in a CSV format for large-scale or batch analysis.
#### 2. **`app.py`**
   - This is the main entry point of the application.
   - It provides the Streamlit-based user interface for uploading log files and viewing analysis results.
   - Handles user interactions such as selecting visualizations and downloading CSV reports.

#### 3. **`utils/`**
   - A directory containing reusable utility scripts for modularity and better code organization.
   - **`log_analyzer.py`**: Includes core logic for:
     - Validating log file format.
     - Parsing logs into a structured DataFrame.
     - Analyzing requests per IP, detecting suspicious activity, and identifying the most accessed endpoints.
   - **`visualizations.py`**: Contains all visualization-related functions, such as:
     - Generating line plots for traffic over time.
     - Bar charts for status code distributions.
     - Heatmaps for failed login attempts.
     - Bar charts for endpoint access.

#### 4. **`temp/`**
   - A directory created dynamically to store uploaded files temporarily.
   - Files in this directory are used for processing during the app's runtime and can be safely deleted after the session ends.

#### 5. **`requirements.txt`**
   - Specifies all the Python libraries and dependencies required to run the application.
   - Install dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

---



## Requirements

- Python 3.8 or later
- Required Python packages:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `streamlit`

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/156sow/VRV-Assignment.git
   cd Web_App
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Upload your log file (in `.log` format) via the provided interface.
4. Explore traffic patterns, detect anomalies, and generate reports.

## File Structure
-
- `app.py`: Main application file.
- `utils/`: Contains helper modules for log validation, parsing, analysis, and visualization.
- `temp/`: Temporary storage for uploaded files.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation file.


## Example

Here is an example of the log file format that the tools in this repository expect:

```bash
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:37 +0000] "GET /contact HTTP/1.1" 200 312
198.51.100.23 - - [03/Dec/2024:10:12:38 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:39 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:40 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:41 +0000] "GET /dashboard HTTP/1.1" 200 1024
198.51.100.23 - - [03/Dec/2024:10:12:42 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:43 +0000] "GET /dashboard HTTP/1.1" 200 1024
```

### Output for the **log_analyzer.py**

#### Request per IP Address
```bash
   IP Address      Request Count
  203.0.113.5             15
  198.51.100.23           8
  192.168.1.1             7
  10.0.0.2                6
  192.168.1.100           5
```
#### Most Frequently Accessed Endpoint
```bash
Endpoint: /login (Accessed 13 times)
```

#### Suspicious Activity Detected (Failed Login Attempts)
```bash
   IP Address      Failed Login Count
  203.0.113.5             15
```


## Visualizations

- **Requests Over Time**: Understand traffic trends with time-series visualizations.
  ![image](https://github.com/user-attachments/assets/5b619efb-9dde-4ba6-95ae-ee79359c6078)
- **HTTP Status Code Distribution**: View the frequency of different status codes.
  ![image](https://github.com/user-attachments/assets/c8547010-cad4-48bd-a11a-15c13649cdd1)
- **Endpoint Access**: Discover the most frequently accessed endpoints.
  ![image](https://github.com/user-attachments/assets/89dc86d8-c179-454f-be57-17fc4c29c945)
- **Failed Login Heatmap**: Identify patterns in failed login attempts.
  ![image](https://github.com/user-attachments/assets/d36c94d2-2658-4ef3-b04a-be7d4f44e8ab)



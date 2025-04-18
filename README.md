# 🔍 Log Analyzer - Streamlit App

This is a simple web application built with **Streamlit** that allows you to upload and analyze log files (`.txt`, `.log`). It scans the logs for potential security 
threats like **failed logins** or **unauthorized access attempts**.


## 🚀 Features

- Upload `.txt` or `.log` files
- View raw log entries
- Detect and highlight suspicious activity:
  - Failed login attempts
  - Unauthorized access
- Easy-to-use interface
  # 🛠️ Setup Instructions

## 1. Clone the Repository
git clone https://github.com/your-username/loganalyser.git
cd loganalyser
## 2. Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate
## 3. Install Dependencies
pip install streamlit pandas
## 4. Run the app
streamlit run app.py
Open the app in your browser at http://localhost:8501
## How Threats Are Detected
The app looks for suspicious log entries using simple pattern matching:

"failed login"

"unauthorized access"

You can customize the logic in util/helpers.py to suit your needs.

# Screenshots
![log analyser](https://github.com/user-attachments/assets/8d5ca190-92a7-4c24-b4d9-fa8eb186905c)




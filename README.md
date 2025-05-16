# 🌲 Wildfire Data Dashboard

This project collects and visualizes wildfire recovery data using datasets from **Kaggle** (CSV files) and **public government wildfire APIs** (e.g., debris removal, parcel eligibility). The goal is to analyze and display real-time and historical wildfire impact and cleanup efforts across communities.

---

## 🔧 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Data Sources:** Kaggle datasets, public wildfire-related APIs

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

- Open **Git Bash** (or Terminal on macOS) and navigate to your desired directory:

- git clone https://github.com/eanyakpor/wildfire-data

- cd wildfire-data

### 2. Install python and pip 

- for windows: Download Python from https://www.python.org/downloads/

- for mac os brew install python3 

- to check if installed run these commands on terminal 

```
python --version
pip --version
```

### 3. Set up VENV

- You can follow this guide:
[How To Setup A Virtual Environment For Python In Visual Studio Code (2023)](https://www.youtube.com/watch?v=GZbeL5AcTgw)

### 4. Install Python Dependencies

```
pip install -r requirements.txt
```

### 5. Add Environment Variables

- Create a .env file in the project root. Paste the variables shared in our Slack channel.

### How to Add a New Table to the Database 

1.	Create a RawData/ folder (if not already created):
	- Place any new .csv files you’d like to upload into this folder.
	- This folder is excluded in .gitignore to prevent CSVs from being committed (especially useful if the data becomes sensitive in the future).

2.	Update the table_schemas dictionary in the Python script:
    - The exact filename (must match what’s in RawData/)
    - The name of the SQL table you want to create
    - The columns you want to upload, with their PostgreSQL data types

- Example:

```
table_schemas = {
    "My_New_Data.csv": {
        "table_name": "my_new_table",
        "columns": {
            "ColumnA": "TEXT",
            "ColumnB": "INTEGER",
            "Timestamp": "DATE"
        }
    }
}
```
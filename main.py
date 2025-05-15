import pandas as pd
import psycopg2
import os 
from dotenv import load_dotenv

# establishing connection with database to upload tables to AWS 

load_dotenv()

connection = psycopg2.connect(
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASS"),
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT")
)

# define the pointer that will execute sql commands 

cursor = connection.cursor()

# add extra csv or csv column headers here for data upload 

table_schemas = {
    "California_Historic_Fire_Perimeters_-6236829869961296710.csv": {
        "table_name": "fire_perimeter",
        "columns": {
            "Year": "INTEGER",
            "State": "TEXT",
            "Fire_Name": "TEXT",
            "GIS_Calculated_Acres": "DOUBLE PRECISION",
            "Cause": "INTEGER",
        }
    },
    "California_Fire_Incidents.csv": {
        "table_name": "incident_details",
        "columns": {
            "Name": "TEXT",
            "Started": "DATE",
            "AcresBurned": "DOUBLE PRECISION",
            "Injuries": "INTEGER",
            "Fatalities": "INTEGER",
            "CountyIds": "TEXT",

        }
    }
}

# create table in python using the cursor for sql commands 

def create_table(cursor, table_name, columns):
    
    # print('cols type', type(columns))
    # print('should be a map',columns)
    # create tuple of array of each (col, dtype)
    col_defs = [f'"{col}" {dtype}' for col, dtype in columns.items()]

    # sql command to create table if it doesn't already exist
    create_sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
    { ', '.join(col_defs)}
    );
    """
    cursor.execute(create_sql)

# loop through tables in table_scemas map and create tables for each of them as defined in table_scemas 

for csv_file, config in table_schemas.items():
    table_name = config["table_name"]
    columns = config["columns"]

    create_table(cursor, table_name, columns)
    print(f"Created table '{table_name}'")


connection.commit()
cursor.close()
connection.close()

import pandas as pd 
import psycopg2 
import os 
from dotenv import load_dotenv
from io import StringIO

load_dotenv()
file_path_str = os.getenv("FILEPATH") #for a new dataset change the last part of this code, to give custom names: fire_data_df = change_names(fire_data_df) 
fire_data_df = pd.read_csv(file_path_str)
print(len(fire_data_df))

# info needed to connect to database 
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
# Connect to PostgreSQL
connection = psycopg2.connect(host = db_host, database = db_name, user = db_user, password = db_pass)

# Create a cursor
cur = connection.cursor()


# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS test_table2 (
    OBJECTID_1 INTEGER,
    OBJECTID INTEGER,
    YEAR INTEGER,
    FIRE_NAME VARCHAR(100),
    GIS_ACRES DECIMAL,
    Shape_Leng DECIMAL,
    Shape__Area DECIMAL,
    Shape__Length DECIMAL
            
);
""")
print("table creation done")
cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'test_table2');")
table_exists = cur.fetchone()[0]
print("Table exists:", table_exists)
# Check actual table columns in PostgreSQL
cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'test_table2' ORDER BY ordinal_position;")
db_columns = [col[0] for col in cur.fetchall()]
print("Database columns:", db_columns)
# Prepare data for copying
print(fire_data_df.columns)
buffer = StringIO()
fire_data_df.to_csv(buffer, index=False, header=False)
buffer.seek(0)
columns_tuple = tuple([name.lower() for name in fire_data_df.columns])
# Use COPY_FROM to insert data
cur.copy_from(buffer, 'test_table2', sep=',', columns=columns_tuple)
 #change this section to match lines 37-40

# Commit and close
print("copy step done")
connection.commit()
print("commit step done")
cur.close()
connection.close()

# OBJECTID_1,OBJECTID,YEAR,FIRE_NAME,GIS_ACRES,Shape_Leng,Shape__Area,Shape__Length
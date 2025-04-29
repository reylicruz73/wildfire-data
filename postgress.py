import psycopg2 
import os 
from dotenv import load_dotenv

load_dotenv()
# info needed to connect to database 
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

connection = psycopg2.connect(host = db_host, database = db_name, user = db_user, password = db_pass)

# after sucessfully conencting to the databse 
print('Connected to the database')

# cursor is a pointer to perform databse manipulation operations 
cursor = connection.cursor()
cursor.execute('SELECT version();')
db_version = cursor.fetchone()
print(db_version)

# must close the connection after use 
cursor.close()

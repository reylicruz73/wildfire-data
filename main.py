import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()
folder = os.getenv("FOLDER")
filename = os.getenv("FILENAME")

path = os.path.join(folder, filename)
test_csv = pd.read_csv(path)
print(test_csv.head())

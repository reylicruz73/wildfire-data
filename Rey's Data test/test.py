url = "/Users/reylicruz/PycharmProjects/wildfire-data/Rey's Data test/mapdataall (1).csv"

import pandas as pd 

df = pd.read_csv(url)

#Get our data information #
# print(df.info())
# print(df.head())
# print(df.describe())
# print(df.columns)


#_________________________________________________________________
#GRAPH 1 Containment vs. Acres Burned 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
url = "/Users/reylicruz/PycharmProjects/wildfire-data/Rey's Data test/mapdataall (1).csv"
df = pd.read_csv(url)

# Clean: only include fires with valid acreage
df = df[df['incident_acres_burned'] > 0]

# Get top 10 largest fires
top10 = df.sort_values(by='incident_acres_burned', ascending=False).head(10)

# Sort for better bar layout
top10 = top10.sort_values(by='incident_acres_burned')

# Plot
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.barplot(
    data=top10,
    x='incident_acres_burned',
    y='incident_name',
    palette='Reds_r'
)

plt.title('🔥 Top 10 Largest Wildfires by Acres Burned')
plt.xlabel('Acres Burned')
plt.ylabel('Fire Name')
plt.tight_layout()
plt.show()

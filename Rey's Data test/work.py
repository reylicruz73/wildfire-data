import pandas as pd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os
import warnings
from mpl_toolkits.mplot3d import Axes3D


warnings.filterwarnings("ignore")

df = pd.read_csv("/Users/reylicruz/PycharmProjects/wildfire-data/data/LACoFDHistoricFirePerimeters.csv")

#TO find our data types
# print(df.columns)
# print(df.dtypes)


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x = df['YEAR']
# y = df['GIS_ACRES']
# z = df['Shape_Leng']

# ax.scatter(x, y, z, c='red', alpha=0.6)
# ax.set_xlabel('Year')
# ax.set_ylabel('Acres Burned')
# ax.set_zlabel('Perimeter Length')
# plt.title("3D Scatter: Fires Over Time")
# plt.show()

#________________________________________
# Create grid
# x = np.linspace(-8, 8, 200)
# y = np.linspace(-8, 8, 200)
# X, Y = np.meshgrid(x, y)

# # Define the function z = sin(x) * cos(y)
# Z = np.sin(X) * np.cos(Y)

# # Set up 3D figure
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import griddata
# from mpl_toolkits.mplot3d import Axes3D

# # Load your fire perimeter data
# df = pd.read_csv("/Users/reylicruz/PycharmProjects/wildfire-data/data/LACoFDHistoricFirePerimeters.csv")

# # Drop rows with missing data
# df = df.dropna(subset=["YEAR", "GIS_ACRES", "Shape_Leng"])

# # Use simplified data
# x = df['YEAR'].values
# y = df['Shape_Leng'].values  # we use Shape_Leng as spatial proxy
# z = df['GIS_ACRES'].values   # fire size

# # Create a grid to interpolate to
# xi = np.linspace(min(x), max(x), 100)
# yi = np.linspace(min(y), max(y), 100)
# XI, YI = np.meshgrid(xi, yi)

# # Interpolate Z values onto the grid
# ZI = griddata((x, y), z, (XI, YI), method='cubic')

# # Plotting
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111, projection='3d')

# # Surface plot
# surf = ax.plot_surface(XI, YI, ZI, cmap='viridis', alpha=0.9)

# # Base plane for visual depth
# ax.plot_surface(XI, YI, np.zeros_like(ZI), color='purple', alpha=0.3)

# # Labels and title
# ax.set_title("3D Surface of LA County Fire History", fontsize=14)
# ax.set_xlabel("Year")
# ax.set_ylabel("Shape Length (Perimeter Proxy)")
# ax.set_zlabel("GIS Acres (Burned Area)")
# plt.tight_layout()
# plt.show()

#________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load fire data
df = pd.read_csv("/Users/reylicruz/PycharmProjects/wildfire-data/data/LACoFDHistoricFirePerimeters.csv")

# Drop missing
df = df.dropna(subset=["GIS_ACRES", "Shape_Leng"])

# Perform linear regression
x = df["Shape_Leng"]
y = df["GIS_ACRES"]
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Predicted line
y_pred = slope * x + intercept

# Start plot
plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(x, y, alpha=0.5, label='Data', color='purple')

# Regression line
plt.plot(x, y_pred, color='red', label='Best-fit line')

# Title and labels
plt.title("Linear Regression: Burned Area vs Fire Perimeter")
plt.xlabel("Shape_Leng (Perimeter)")
plt.ylabel("GIS_ACRES (Burned Area)")
plt.legend()

# Annotate regression math on the side
eq_text = (
    f"y = {slope:.2f}x + {intercept:.2f}\n"
    f"R² = {r_value**2:.3f}\n"
    f"P-value = {p_value:.3e}\n"
)

if r_value**2 > 0.7:
    corr_strength = "strong"
elif r_value**2 > 0.4:
    corr_strength = "moderate"
elif r_value**2 > 0.2:
    corr_strength = "weak"
else:
    corr_strength = "very weak"

eq_text += f"Correlation: {corr_strength}"

# Place text box on plot
plt.text(x.max()*0.6, y.max()*0.7, eq_text, fontsize=12,
         bbox=dict(facecolor='white', edgecolor='black'))

plt.tight_layout()
plt.show()

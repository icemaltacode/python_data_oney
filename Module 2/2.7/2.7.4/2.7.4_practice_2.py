"""
Encoding time by color
=====================

The screen only has two dimensions, but we can encode another dimension in the scatter plot using color. 
Here, we will visualize the climate_change dataset, plotting a scatter plot of the "co2" column, on the x-axis, 
against the "relative_temp" column, on the y-axis. We will encode time using the color dimension, 
with earlier times appearing as darker shades of blue and later times appearing as brighter shades of yellow.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv('Module 2/data/climate_change.csv')
# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Using the ax.scatter method add a scatter plot of the "co2" column (x-axis) against the "relative_temp" column.
# Use the c key-word argument to pass in the index of the DataFrame as input to color each point according to its date.
____

# Set the x-axis label to "CO2 (ppm)"
____

# Set the y-axis label to "Relative temperature (C)"
____

plt.show()
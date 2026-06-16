"""
Simple scatter plot
===================

Scatter are a bi-variate visualization technique. They plot each record in the data as a point. 
The location of each point is determined by the value of two variables: the first variable determines 
the distance along the x-axis and the second variable determines the height along the y-axis.

In this exercise, you will create a scatter plot of the climate_change data. This DataFrame, which is 
already loaded, has a column "co2" that indicates the measurements of carbon dioxide every month and 
another column, "relative_temp" that indicates the temperature measured at the same time.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv('Module 2/data/climate_change.csv')
# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Using the ax.scatter method, add the data to the plot: "co2" on the x-axis and "relative_temp" on the y-axis.
____

# Set the x-axis label to "CO2 (ppm)".
____

# Set the y-axis label to "Relative temperature (C)"
____

plt.show()
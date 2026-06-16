"""
Plotting two variables
======================

If you want to plot two time-series variables that were recorded at the same times, you can add both of them to 
the same subplot.

If the variables have very different scales, you'll want to make sure that you plot them in different twin 
Axes objects. These objects can share one axis (for example, the time, or x-axis) while not sharing the 
other (the y-axis).

To create a twin Axes object that shares the x-axis, we use the twinx method.

In this exercise, you'll have access to a DataFrame that has the climate_change data loaded into it. 
This DataFrame was loaded with the "date" column set as a DateTimeIndex, and it has a column called "co2" 
with carbon dioxide measurements and a column called "relative_temp" with temperature measurements.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv("Module 2/data/climate_change.csv", parse_dates=["date"], index_col=["date"])
# endregion

## ---- START HERE ----

# Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.
____

# Plot the carbon dioxide variable in blue using the Axes plot method.
ax.plot(____, ____, color=____)

# Use the Axes twinx method to create a twin Axes that shares the x-axis.
ax2 = ____

# Plot the relative temperature variable in red on the twin Axes using its plot method.
____.plot(____, ____, color=____)

plt.show()
"""
Plot time-series data
=====================

To plot time-series data, we use the Axes object plot command. The first argument to this method are the values 
for the x-axis and the second argument are the values for the y-axis.

This exercise provides data stored in a DataFrame called climate_change. This variable has a time-index 
with the dates of measurements and two data columns: "co2" and "relative_temp".

In this case, the index of the DataFrame would be used as the x-axis values and we will plot the 
values stored in the "relative_temp" column as the y-axis values. We will also properly label the 
x-axis and y-axis.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv("Module 2/data/climate_change.csv", parse_dates=["date"], index_col=["date"])
# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Add the data from climate_change to the plot: use the DataFrame index for the x value 
# and the "relative_temp" column for the y values.
____

# Set the x-axis label to 'Time'.
____

# Set the y-axis label to 'Relative temperature (Celsius)'.
____

# Show the figure
____
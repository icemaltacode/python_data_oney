"""
Using a time index to zoom in
=============================

When a time-series is represented with a time index, we can use this index for the x-axis when plotting. 
We can also select a range of dates to zoom in on a particular period within the time-series using 
pandas' indexing facilities. In this exercise, you will select a portion of a time-series dataset and 
you will plot that period.

The data to use is stored in a DataFrame called climate_change, which has a time-index with dates of 
measurements and two data columns: "co2" and "relative_temp".
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv("Module 2/data/climate_change.csv", parse_dates=["date"], index_col=["date"])
# endregion

## ---- START HERE ----

# Use plt.subplots to create a Figure with one Axes called fig and ax, respectively.
____

# Create a variable called seventies that includes all the data between "1970-01-01" and "1979-12-31".
seventies = climate_change[____]

# Add the data from seventies to the plot: use the DataFrame index for the x value and 
# the "co2" column for the y values.
____(____, ____["co2"])

# Show the figure
____
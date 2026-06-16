"""
Annotating a plot of time-series data
=====================================

Annotating a plot allows us to highlight interesting information in the plot. 
For example, in describing the climate change dataset, we might want to point to the date at which the 
relative temperature first exceeded 1 degree Celsius.

For this, we will use the annotate method of the Axes object. In this exercise, you will have the 
DataFrame called climate_change loaded into memory. Using the Axes methods, plot only the relative 
temperature column as a function of dates, and annotate the data.

"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv("Module 2/data/climate_change.csv", parse_dates=["date"], index_col=["date"])
# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Use the ax.plot method to plot the DataFrame index against the relative_temp column.
____

# Use the annotate method to add the text '>1 degree' in the location (pd.Timestamp('2015-10-06'), 1).
ax.____(____, ____)

plt.show()

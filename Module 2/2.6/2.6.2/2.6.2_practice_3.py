"""
Using a plotting function
=========================

Defining functions allows us to reuse the same code without having to repeat all of it. 
Programmers sometimes say "Don't repeat yourself".

In the previous exercise, you defined a function called plot_timeseries:

```
plot_timeseries(axes, x, y, color, xlabel, ylabel)
```

that takes an Axes object (as the argument axes), time-series data (as x and y arguments) the name of a color 
(as a string, provided as the color argument) and x-axis and y-axis labels (as xlabel and ylabel arguments). 
In this exercise, the function plot_timeseries is already defined and provided to you.

Use this function to plot the climate_change time-series data, provided as a pandas DataFrame object that has 
a DateTimeIndex with the dates of the measurements and co2 and relative_temp columns.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv("Module 2/data/climate_change.csv", parse_dates=["date"], index_col=["date"])

def plot_timeseries(axes, x, y, color, xlabel, ylabel):
  axes.plot(x, y, color=color)
  axes.set_xlabel(xlabel)
  axes.set_ylabel(ylabel, color=color)
  axes.tick_params('y', colors=color)
# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# In the provided ax object, use the function plot_timeseries to plot the "co2" column in blue, 
# with the x-axis label "Time (years)" and y-axis label "CO2 levels".
____(____, ____, ____, "blue", ____, ____)

# Use the ax.twinx method to add an Axes object to the figure that shares the x-axis with ax.
ax2 = ____

# Use the function plot_timeseries to add the data in the "relative_temp" column in red to the 
# twin Axes object, with the x-axis label "Time (years)" and y-axis label "Relative temperature (Celsius)".
____(____, ____, ____, "red", ____, ____)

plt.show()

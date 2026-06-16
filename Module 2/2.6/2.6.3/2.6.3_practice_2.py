"""
Plotting time-series: putting it all together
=============================================

In this exercise, you will plot two time-series with different scales on the same Axes, and annotate the 
data from one of these series.

The CO2/temperatures data is provided as a DataFrame called climate_change. You should also use the function 
that we have defined before, called plot_timeseries, which takes an Axes object (as the axes argument) plots 
a time-series (provided as x and y arguments), sets the labels for the x-axis and y-axis and sets the color 
for the data, and for the y tick/axis labels:

```
plot_timeseries(axes, x, y, color, xlabel, ylabel)
```

Then, you will annotate with text an important time-point in the data: on 2015-10-06, when the temperature 
first rose to above 1 degree over the average.

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

# Use the plot_timeseries function to plot CO2 levels against time. Set xlabel to "Time (years)" ylabel to 
# "CO2 levels" and color to 'blue'.
plot_timeseries(____, ____, ____, 'blue', ____, ____)

# Create ax2, as a twin of the first Axes.
ax2 = ____

# In ax2, plot temperature against time, setting the color ylabel to "Relative temp (Celsius)" and color to 'red'.
plot_timeseries(____, ____, ____, 'red', ____, ____)

# Annotate the data using the ax2.annotate method. Place the text ">1 degree" in x=pd.Timestamp('2008-10-06'), 
# y=-0.2 pointing with a gray thin arrow to x=pd.Timestamp('2015-10-06'), y = 1.
ax2.____(">1 degree", ____, ____, ____)

plt.show()

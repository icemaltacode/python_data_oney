"""
Small multiples with shared y axis
==================================

When creating small multiples, it is often preferable to make sure that the different plots are 
displayed with the same scale used on the y-axis. This can be configured by setting the sharey 
key-word to True.

In this exercise, you will create a Figure with two Axes objects that share their y-axis. 
As before, the data is provided in seattle_weather and austin_weather DataFrames.
"""

# region setup
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize'] = (10, 5)
seattle_weather = pd.read_csv('Module 2/data/seattle_weather.csv', index_col='DATE')
austin_weather = pd.read_csv('Module 2/data/austin_weather.csv', index_col='DATE')
# endregion

# Create a Figure with an array of two Axes objects that share their y-axis range.
fig, ax = plt.subplots(2, 1, sharey=True)

## ---- START HERE ----

# Plot Seattle's "MLY-PRCP-NORMAL" in a solid blue line in the top Axes. 
____.plot(____, ____, color = ____)

# Add Seattle's "MLY-PRCP-25PCTL" and "MLY-PRCP-75PCTL" in dashed blue lines to the top Axes.
____.plot(____, ____, color = ____, linestyle = ____)
____.plot(____, ____, color = ____, linestyle = ____)

# Plot Austin's "MLY-PRCP-NORMAL" in a solid red line in the bottom Axes and the "MLY-PRCP-25PCTL"
# and "MLY-PRCP-75PCTL" in dashed red lines.
____.plot(____, ____, color = ____)
____.plot(____, ____, color = ____, linestyle = ____)
____.plot(____, ____, color = ____, linestyle = ____)

# Show the plot
plt.show()
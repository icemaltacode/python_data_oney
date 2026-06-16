"""
Adding error-bars to a plot
===========================

Adding error-bars to a plot is done by using the errorbar method of the Axes object.

Here, you have two DataFrames loaded: seattle_weather has data about the weather in Seattle and 
austin_weather has data about the weather in Austin. Each DataFrame has a column "MONTH" that has the names 
of the months, a column "MLY-TAVG-NORMAL" that has the average temperature in each month and a column 
"MLY-TAVG-STDDEV" that has the standard deviation of the temperatures across years.

In the exercise, you will plot the mean temperature across months and add the standard deviation at each point 
as y errorbars.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
seattle_weather = pd.read_csv('Module 2/data/seattle_weather.csv', index_col='DATE')
austin_weather = pd.read_csv('Module 2/data/austin_weather.csv', index_col='DATE')

# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Use the ax.errorbar method to add the Seattle data: the "MONTH" column as x values, 
# the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
ax.errorbar(____, ____, ____)

# Add the Austin data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values 
# and "MLY-TAVG-STDDEV" as yerr values.
____ 

# Set the y-axis label as "Temperature (Fahrenheit)".
____

plt.show()

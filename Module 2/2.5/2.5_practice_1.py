"""
Creating small multiples with plt.subplots
==========================================

Small multiples are used to plot several datasets side-by-side. In Matplotlib, small multiples can be created using 
the plt.subplots() function. The first argument is the number of rows in the array of Axes objects generate and the 
second argument is the number of columns. In this exercise, you will use Austin and Seattle weather data to practice 
creating and populating an array of subplots.

The data is given to you in DataFrames: seattle_weather and austin_weather. 
These each have a "MONTH" column and "MLY-PRCP-NORMAL" (for average precipitation), as well as "MLY-TAVG-NORMAL" 
(for average temperature) columns. In this exercise, you will plot in a separate subplot the monthly average precipitation 
and average temperatures in each city.
"""

# region setup
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['figure.figsize'] = (10, 5)
seattle_weather = pd.read_csv('Module 2/data/seattle_weather.csv', index_col='DATE')
austin_weather = pd.read_csv('Module 2/data/austin_weather.csv', index_col='DATE')
# endregion

## ---- START HERE ----

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(____, ____)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(____, ____)

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(____, ____)

# In the bottom left (1, 0) plot month and Austin precipitations
ax[____].plot(____, ____)

# In the bottom right (1, 1) plot month and Austin temperatures
ax[____].plot(____, ____)
plt.show()
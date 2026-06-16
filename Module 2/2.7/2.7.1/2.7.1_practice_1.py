"""
Bar chart
=========

Bar charts visualize data that is organized according to categories as a series of bars, where the height of 
each bar represents the values of the data in this category.

For example, in this exercise, you will visualize the number of gold medals won by each country in the provided 
medals DataFrame. The DataFrame contains the countries as the index, and a column called "Gold" that contains 
the number of gold medals won by each country, according to their rows.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
medals = pd.read_csv('Module 2/data/medals.csv', index_col=0)
# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Call the ax.bar method to plot the "Gold" column as a function of the country.
____

# Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.
# In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by 
# using the rotation key-word argument.
____.set_xticklabels(____, ____)

# Set the y-axis label to "Number of medals".
____

plt.show()
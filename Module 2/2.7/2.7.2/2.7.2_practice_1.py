"""
Creating histograms
===================

Histograms show the full distribution of a variable. In this exercise, we will display the distribution of 
weights of medalists in gymnastics and in rowing in the 2016 Olympic games for a comparison between them.

You will have two DataFrames to use. The first is called mens_rowing and includes information about the 
medalists in the men's rowing events. The other is called mens_gymnastics and includes information about 
medalists in all of the Gymnastics events.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
mens_rowing = pd.read_csv('Module 2/data/mens_rowing.csv', index_col=0)
mens_gymnastics = pd.read_csv('Module 2/data/mens_gymnastics.csv', index_col=0)

# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Use the ax.hist method to add a histogram of the "Weight" column from the mens_rowing DataFrame.
ax.hist(____)

# Use ax.hist to add a histogram of "Weight" for the mens_gymnastics DataFrame.
____

# Set the x-axis label to "Weight (kg)" and the y-axis label to "# of observations".

# Set the x-axis label
____

# Set the y-axis label
____

plt.show()
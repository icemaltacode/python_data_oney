"""
Adding error-bars to a bar chart
================================

Statistical plotting techniques add quantitative information for comparisons into the visualization. 
For example, in this exercise, we will add error bars that quantify not only the difference in the means 
of the height of medalists in the 2016 Olympic Games, but also the standard deviation of each of these groups, 
as a way to assess whether the difference is substantial relative to the variability within each group.

For the purpose of this exercise, you will have two DataFrames: mens_rowing holds data about the medalists 
in the rowing events and mens_gymnastics will hold information about the medalists in the gymnastics events.
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

# Add a bar with size equal to the mean of the "Height" column in the mens_rowing 
# DataFrame and an error-bar of its standard deviation.
ax.____("Rowing", ____, yerr=____)

# Add another bar for the mean of the "Height" column in mens_gymnastics with an 
# error-bar of its standard deviation.
____

# Add a label to the the y-axis: "Height (cm)".
____

plt.show()

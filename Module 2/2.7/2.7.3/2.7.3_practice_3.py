"""
Creating boxplots
=================

Boxplots provide additional information about the distribution of the data that they represent. 
They tell us what the median of the distribution is, what the inter-quartile range is and also what 
the expected range of approximately 99% of the data should be. Outliers beyond this range are particularly 
highlighted.

In this exercise, you will use the data about medalist heights that you previously visualized as histograms, 
and as bar charts with error bars, and you will visualize it as boxplots.

Again, you will have the mens_rowing and mens_gymnastics DataFrames available to you, and both of these 
DataFrames have columns called "Height" that you will compare.
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

# Create a boxplot that contains the "Height" column for mens_rowing on the left and mens_gymnastics on the right.
____

# Add x-axis tick labels: "Rowing" and "Gymnastics".
____

# Add a y-axis label: "Height (cm)".
____

plt.show()

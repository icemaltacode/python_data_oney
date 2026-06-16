"""
Save a figure with different sizes
==================================

Before saving your visualization, you might want to also set the size that the figure will 
have on the page. To do so, you can use the Figure object's set_size_inches method. 
This method takes a sequence of two values. The first sets the width and the second sets 
the height of the figure.

Here, you will again have a Figure object called fig already provided (you can run plt.show 
if you want to see its contents). Use the Figure methods set_size_inches and savefig to 
change its size and save two different versions of this figure.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
medals = pd.read_csv('Module 2/data/medals.csv', index_col=0)
medals['Total'] = medals['Bronze'] + medals['Silver'] + medals['Gold']
fig, ax = plt.subplots()
ax.bar(medals.index, medals['Gold'])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel('Number of medals')
# endregion

## ---- START HERE ----

# 1
# Set the figure size as width of 3 inches and height of 5 inches and 
# save it as 'figure_3_5.png' with default resolution.
____

# 2
# Set the figure size to width of 5 inches and height of 3 inches and 
# save it as 'figure_5_3.png' with default settings.
____

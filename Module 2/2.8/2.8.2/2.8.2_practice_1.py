"""
Saving a file several times
===========================

If you want to share your visualizations with others, you will need to save them into files. 
Matplotlib provides as way to do that, through the savefig method of the Figure object. 
In this exercise, you will save a figure several times. Each time setting the parameters to something 
slightly different. We have provided and already created Figure object.
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
# Examine the figure by calling the plt.show() function.
____

# 2
# Save the figure into the file my_figure.png, using the default resolution.
____

# 3
# Save the figure into the file my_figure_300dpi.png and set the resolution to 300 dpi.
____
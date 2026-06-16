"""
Stacked bar chart
=================

A stacked bar chart contains bars, where the height of each bar represents values. In addition, stacked on top 
of the first variable may be another variable. The additional height of this bar represents the value of this 
variable. And you can add more bars on top of that.

In this exercise, you will have access to a DataFrame called medals that contains an index that holds the names 
of different countries, and three columns: "Gold", "Silver" and "Bronze". You will also have a Figure, fig, and 
Axes, ax, that you can add data to.

You will create a stacked bar chart that shows the number of gold, silver, and bronze medals won by each country,
 and you will add labels and create a legend that indicates which bars represent which medals.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
medals = pd.read_csv('Module 2/data/medals.csv', index_col=0)
fig, ax = plt.subplots()
# endregion

## ---- START HERE ----

# Call the ax.bar method to add the "Gold" medals. Call it with the label set to "Gold".
____(____, ____, label=____)

# Call the ax.bar method to stack "Silver" bars on top of that, using the bottom key-word argument so the 
# bottom of the bars will be on top of the gold medal bars, and label to add the label "Silver".
____(____, ____, bottom=____, ____)

# Use ax.bar to add "Bronze" bars on top of that, using the bottom key-word and label it as "Bronze".
____

# Display the legend
ax.legend()

plt.show()
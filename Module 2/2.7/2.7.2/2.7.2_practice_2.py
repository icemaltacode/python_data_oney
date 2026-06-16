"""
"Step" histogram
================

Histograms allow us to see the distributions of the data in different groups in our data. In this exercise, 
you will select groups from the Summer 2016 Olympic Games medalist dataset to compare the height of medalist 
athletes in two different sports.

The data is stored in a pandas DataFrame object called summer_2016_medals that has a column "Height". 
In addition, you are provided a pandas GroupBy object that has been grouped by the sport.

In this exercise, you will visualize and label the histograms of two sports: "Gymnastics" and "Rowing" 
and see the marked difference between medalists in these two sports.
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

# Use the hist method to display a histogram of the "Weight" column from the mens_rowing DataFrame, 
# label this as "Rowing". 
# Use the histtype argument to visualize the data using the 'step' type and set the number of bins to use to 5.
____

# Use hist to display a histogram of the "Weight" column from the mens_gymnastics DataFrame, and label 
# this as "Gymnastics".
# # Use the histtype argument to visualize the data using the 'step' type and set the number of bins to use to 5.
____

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
____
plt.show()

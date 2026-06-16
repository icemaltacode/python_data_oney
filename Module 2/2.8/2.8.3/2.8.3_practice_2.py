"""
Automate your visualisation
===========================

One of the main strengths of Matplotlib is that it can be automated to adapt to the data that 
it receives as input. For example, if you receive data that has an unknown number of 
categories, you can still create a bar plot that has bars for each category.

This is what you will do in this exercise. You will be visualising data about medal winners 
in the 2016 summer Olympic Games again, but this time you will have a dataset that has some 
unknown number of branches of sports in it. This will be loaded into memory as a pandas 
DataFrame object called summer_2016_medals, which has a column called "Sport" that tells 
you to which branch of sport each row corresponds. There is also a "Weight" column that 
tells you the weight of each athlete.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
summer_2016_medals = pd.read_csv('Module 2/data/summer_2016_medals.csv', index_col=0)
sports_column = summer_2016_medals['Sport']
sports = sports_column.unique()
# endregion

fig, ax = plt.subplots()

## ---- START HERE ----

# Iterate over the values of sports setting sport as your loop variable.
for ____ in ____:
  # In each iteration, extract the rows where the "Sport" column is equal to sport.
  sport_df = ____
  # Add a bar to the provided ax object, labeled with the sport name, with the mean 
  # of the "Weight" column as its height, and the standard deviation as a y-axis error bar.
  ____

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure into the file "sports_weights.png".
____

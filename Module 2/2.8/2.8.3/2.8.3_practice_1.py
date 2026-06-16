"""
Unique values of a column
=========================

One of the main strengths of Matplotlib is that it can be automated to adapt to the data that 
it receives as input. For example, if you receive data that has an unknown number of categories, 
you can still create a bar plot that has bars for each category.

In this exercise and the next, you will be visualizing the weight of athletes in the 2016 
summer Olympic Games again, from a dataset that has some unknown number of branches of sports 
in it. This will be loaded into memory as a pandas DataFrame object called summer_2016_medals,
 which has a column called "Sport" that tells you to which branch of sport each row 
 corresponds. There is also a "Weight" column that tells you the weight of each athlete.

In this exercise, we will extract the unique values of the "Sport" column
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
summer_2016_medals = pd.read_csv('Module 2/data/summer_2016_medals.csv', index_col=0)
# endregion

## ---- START HERE ----

# Create a variable called sports_column that holds the data from the "Sport" column of the DataFrame object.
sports_column = ____

# Use the unique method of this variable to find all the unique different sports that are present in this data, 
# and assign these values into a new variable called sports.
sports = ____

# Print the sports variable to the console.
____
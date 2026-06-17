"""
Using .melt() to reshape government data
========================================

The US Bureau of Labor Statistics (BLS) often provides data series in an easy-to-read 
format - it has a separate column for each month, and each year is a different row. 
Unfortunately, this wide format makes it difficult to plot this information over time. 
In this exercise, you will reshape a table of US unemployment rate data from the BLS 
into a form you can plot using .melt(). You will need to add a date column to the table 
and sort by it to plot the data correctly.

The unemployment rate data has been loaded for you in a table called ur_wide. 
You are encouraged to explore this table before beginning the exercise.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
ur_wide = pd.read_csv('Module 3/data/ur_wide.csv')
# endregion

## ---- START HERE ----

# Use .melt() to unpivot all of the columns of ur_wide except year and ensure that the 
# columns with the months and values are named month and unempl_rate, respectively. 
# Save the result as ur_tall.
ur_tall = ____

# Add a column to ur_tall named date which combines the year and month columns as 
# year-month format into a larger string, and converts it to a date data type.
ur_tall = ur_tall[ur_tall['unempl_rate'] != "nan"].dropna().astype(str)
ur_tall['date'] = pd.to_datetime(ur_tall['____'] + '-' + ____)

# Sort ur_tall by date and save as ur_sorted.
ur_sorted = ____

# Using ur_sorted, plot unempl_rate on the y-axis and date on the x-axis.
ur_sorted['unempl_rate'] = pd.to_numeric(ur_sorted['unempl_rate'])
ur_sorted.plot(____)
plt.show()
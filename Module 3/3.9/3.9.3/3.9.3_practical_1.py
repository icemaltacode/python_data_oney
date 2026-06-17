"""
Subsetting rows with .query()
=============================

In this exercise, you will revisit GDP and population data for Australia and Sweden from 
the World Bank and expand on it using the .query() method. You'll merge the two tables 
and compute the GDP per capita. Afterwards, you'll use the .query() method to sub-select 
the rows and create a plot. Recall that you will need to merge on multiple columns in the 
proper order.

The tables gdp and pop have been loaded for you.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
gdp = pd.read_csv('Module 3/data/gdp4.csv')
gdp["date"] = pd.to_datetime(gdp["date"])
pop = pd.read_csv('Module 3/data/pop2.csv')
pop["date"] = pd.to_datetime(pop["date"])
# endregion

## ---- START HERE ----

# 1
# Use merge_ordered() on gdp and pop on columns country and date with the fill feature, 
# save to gdp_pop and print.
gdp_pop = ____

# 2
# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
___

# 3
# Pivot gdp_pop so values='gdp_per_capita', index='date', and columns='country', 
# save as gdp_pivot.
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', '____', '____')

# 4
# Use .query() to select rows from gdp_pivot where date is greater than equal to 
# "1991-01-01". Save as recent_gdp_pop.
recent_gdp_pop = gdp_pivot.query('____')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()

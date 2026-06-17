"""
merge_ordered() caution, multiple columns
=========================================

When using merge_ordered() to merge on multiple columns, the order is important when you 
combine it with the forward fill feature. The function sorts the merge on columns in the 
order provided. In this exercise, we will merge GDP and population data from the World Bank 
for Australia and Sweden, reversing the order of the merge on columns. The frequency of 
the series are different, the GDP values are quarterly, and the population is yearly. 
Use the forward fill feature to fill in the missing data. Depending on the order provided, 
the fill forward will use unintended data to fill in the missing values.

The tables gdp and pop have been loaded.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
gdp = pd.read_csv('Module 3/data/gdp2.csv')
pop = pd.read_csv('Module 3/data/pop1.csv')
# endregion

## ---- START HERE ----

# 1
# Use merge_ordered() on gdp and pop, merging on columns date and country with the 
# fill feature, save to ctry_date.
ctry_date = pd.merge_ordered(____, 
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

# 2
# Perform the same merge of gdp and pop, but join on country and date (reverse of step 1) 
# with the fill feature, saving this as date_ctry.
date_ctry = ____

# Print date_ctry
print(date_ctry)
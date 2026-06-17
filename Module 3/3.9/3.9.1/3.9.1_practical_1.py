"""
Correlation between GDP and S&P500
==================================

In this exercise, you want to analyze stock returns from the S&P 500. You believe there may
be a relationship between the returns of the S&P 500 and the GDP of the US. Merge the 
different datasets together to compute the correlation.

Two tables have been provided for you, named sp500, and gdp. As always, pandas has been 
imported for you as pd.
"""

# region setup
import pandas as pd
gdp = pd.read_csv('Module 3/data/gdp1.csv')
gdp.columns = gdp.columns.str.lower()
sp500 = pd.read_csv('Module 3/data/S&P500.csv')
sp500.columns = sp500.columns.str.lower()
# endregion

## ---- START HERE ----

# 1 
# Use merge_ordered() to merge gdp and sp500 using a left join where the year column 
# from gdp is matched with the date column from sp500.
gdp_sp500 = pd.merge_ordered(____, ____, left_on=____, right_on=____, 
                             how=____)

# Print gdp_sp500
print(____)

# 2
# Use the merge_ordered() function again, similar to before, to merge gdp and sp500, 
# using the function's ability to fill in missing data for returns by forward-filling 
# the missing values. Assign the resulting table to the variable gdp_sp500.
gdp_sp500 = pd.merge_ordered(____)

# Print gdp_sp500
print (gdp_sp500)

# 3
# Subset the gdp_sp500 table, select the gdp and returns columns, and save as gdp_returns.
gdp_returns = ____

# Print the correlation matrix of the gdp_returns table using the .corr() method.
print (____)

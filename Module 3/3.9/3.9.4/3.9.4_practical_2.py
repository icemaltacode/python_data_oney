"""
Using .melt() for stocks vs bond performance
============================================

It is widespread knowledge that the price of bonds is inversely related to the price of 
stocks. In this last exercise, you'll review many of the topics in this chapter to 
confirm this. You have been given a table of percent change of the US 10-year treasury 
bond price. It is in a wide format where there is a separate column for each year. 
You will need to use the .melt() method to reshape this table.

Additionally, you will use the .query() method to filter out unneeded data. 
You will merge this table with a table of the percent change of the Dow Jones 
Industrial stock index price. Finally, you will plot data.

The tables ten_yr and dji have been loaded for you.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
ten_yr = pd.read_csv('Module 3/data/ten_yr.csv')
dji = pd.read_csv('Module 3/data/dji.csv')
# endregion

## ---- START HERE ----

# Use .melt() on ten_yr to unpivot everything except the metric column, 
# setting var_name='date' and value_name='close'. Save the result to bond_perc.
bond_perc = ____

# Using the .query() method, select only those rows where metric equals close, 
# and save to bond_perc_close.
bond_perc_close = ____

# Use merge_ordered() to merge dji (left table) and bond_perc_close on date with an
# inner join, and set suffixes equal to ('_dow', '_bond'). Save the result to dow_bond
dow_bond = ____

# Using dow_bond, plot only the Dow and bond values.
dow_bond.plot(____, x='date', rot=90)
plt.show()

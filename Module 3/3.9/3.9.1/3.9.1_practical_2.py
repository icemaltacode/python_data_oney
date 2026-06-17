"""
Phillips curve using merge_ordered()
====================================

There is an economic theory developed by A. W. Phillips which states that inflation and 
unemployment have an inverse relationship. The theory claims that with economic growth 
comes inflation, which in turn should lead to more jobs and less unemployment.

You will take two tables of data from the U.S. Bureau of Labor Statistics, containing 
unemployment and inflation data over different periods, and create a Phillips curve. 
The tables have different frequencies. One table has a data entry every six months, 
while the other has a data entry every month. You will need to use the entries where 
you have data within both tables.

The tables unemployment and inflation have been loaded for you.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
inflation = pd.read_csv('Module 3/data/inflation.csv')
unemployment = pd.read_csv('Module 3/data/unemployment.csv')
# endregion

## ---- START HERE ----

# Use merge_ordered() to merge the inflation and unemployment tables on date with an 
# inner join, and save the results as inflation_unemploy.
inflation_unemploy = ____

# Print the inflation_unemploy dataframe.
____

# Using inflation_unemploy, create a scatter plot with unemployment_rate on the 
# horizontal axis and cpi (inflation) on the vertical axis.
inflation_unemploy.plot(____)
plt.show()
"""
Using merge_asof() to create dataset
====================================

The merge_asof() function can be used to create datasets where you have a table of start 
and stop dates, and you want to use them to create a flag in another table. You have been 
given gdp, which is a table of quarterly GDP values of the US during the 1980s. 
Additionally, the table recession has been given to you. It holds the starting date of 
every US recession since 1980, and the date when the recession was declared to be over. 
Use merge_asof() to merge the tables and create a status flag if a quarter was during a 
recession. Finally, to check your work, plot the data in a bar chart.

The tables gdp and recession have been loaded for you.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
gdp = pd.read_csv('Module 3/data/gdp3.csv')
gdp["date"] = pd.to_datetime(gdp["date"])
recession = pd.read_csv('Module 3/data/recession.csv')
recession["date"] = pd.to_datetime(recession["date"])
# endregion

## ---- START HERE ----

# Using merge_asof(), merge gdp and recession on date, with gdp as the left table. 
# Save to the variable gdp_recession.
gdp_recession = ____

# Create a list using a list comprehension and a conditional expression, named 
# is_recession, where for each row if the gdp_recession['econ_status'] value is 
# equal to 'recession' then enter 'r' else 'g'.
is_recession = ['____' if s=='recession' else '____' for s in gdp_recession['econ_status']]

# Using gdp_recession, plot a bar chart of gdp versus date, setting the color 
# argument equal to is_recession.
gdp_recession['date'] = gdp_recession['date'].dt.strftime('%Y-%m-%d')
gdp_recession.plot(kind=____, y=____, x=____, color=____, rot=90)
plt.show()

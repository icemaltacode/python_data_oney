"""
One-to-many merge with multiple tables
======================================

In this exercise, assume that you are looking to start a business in the city of Chicago. 
Your perfect idea is to start a company that uses goats to mow the lawn for other businesses. 
However, you have to choose a location in the city to put your goat farm. 
You need a location with a great deal of space and relatively few businesses and people around to 
avoid complaints about the smell. You will need to merge three tables to help you choose your location. 
The land_use table has info on the percentage of vacant land by city ward. 
The census table has population by ward, and the licenses table lists businesses by ward.

The land_use, census, and licenses tables have been loaded for you.
"""

# region setup
import pandas as pd
land_use = pd.read_pickle('Module 3/data/land_use.p')
census = pd.read_pickle('Module 3/data/census.p').astype(object)
licenses = pd.read_pickle('Module 3/data/licenses.p')
# endregion

## ---- START HERE ----

# 1
# Merge land_use and census on the ward column. Merge the result of this with licenses on the ward 
# column, using the suffix _cen for the left table and _lic for the right table. Save this to the 
# variable land_cen_lic.

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = ____

# 2
# Group land_cen_lic by ward, pop_2010 (the population in 2010), and vacant, then count the number 
# of accounts. Save the results to pop_vac_lic.

pop_vac_lic = land_cen_lic.groupby(____, 
                                   as_index=False).agg({'account':'count'})

# 3
# Sort pop_vac_lic by vacant, account, andpop_2010 in descending, ascending, and ascending order 
# respectively. Save it as sorted_pop_vac_lic.

sorted_pop_vac_lic = pop_vac_lic.sort_values(____, 
                                             ascending=____)

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

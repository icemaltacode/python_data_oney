"""
Three table merge
=================

To solidify the concept of a three DataFrame merge, practice another exercise. A reasonable extension 
of our review of Chicago business data would include looking at demographics information about the 
neighborhoods where the businesses are. A table with the median income by zip code has been provided 
to you. You will merge the licenses and wards tables with this new income-by-zip-code table called 
zip_demo.

The licenses, wards, and zip_demo DataFrames have been loaded for you.
"""

# region setup
import pandas as pd
wards = pd.read_pickle('Module 3/data/ward.p')
licenses = pd.read_pickle('Module 3/data/licenses.p')
zip_demo = pd.read_pickle('Module 3/data/zip_demo.p')
# endregion

## ---- START HERE ----

# Starting with the licenses table, merge to it the zip_demo table on the zip column. 
# Then merge the resulting table to the wards table on the ward column. 
# Save result of the three merged tables to a variable named licenses_zip_ward.
licenses_zip_ward = licenses.merge____ \
            			____

# Group the results of the three merged tables by the column alderman and find the median income.
print(____.groupby(____).agg({'income':'median'}))
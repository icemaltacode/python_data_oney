"""
Read data with a time index
============================

pandas DataFrame objects can have an index denoting time, this recognized by Matplotlib for axis labeling.

This exercise involves reading data from climate_change.csv, containing CO2 levels and temperatures 
recorded on the 6th of each month from 1958 to 2016, using pandas' read_csv function. 
The parse_dates and index_col arguments help set a DateTimeIndex.
"""

# region setup
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
# endregion


## ---- START HERE ----

# Import pandas as pd
____

# Read in the data from a CSV file called 'Module 2/data/climate_change.csv' using pd.read_csv.
# Use the parse_dates key-word argument to parse the "date" column as dates.
# Use the index_col key-word argument to set the "date" column as the index.
climate_change = pd.read_csv(____, ____, ____)
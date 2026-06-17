"""
Using merge_asof() to study stocks
==================================

You have a feed of stock market prices that you record. You attempt to track the price 
every five minutes. Still, due to some network latency, the prices you record are roughly 
every 5 minutes. You pull your price logs for three banks, JP Morgan (JPM), 
Wells Fargo (WFC), and Bank Of America (BAC). You want to know how the price change of 
the two other banks compare to JP Morgan. Therefore, you will need to merge these three 
logs into one table. Afterward, you will use the pandas .diff() method to compute the 
price change over time. Finally, plot the price changes so you can review your analysis.

The three log files have been loaded for you as tables named jpm, wells, and bac.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
jpm = pd.read_csv('Module 3/data/jpm.csv')
jpm["date_time"] = pd.to_datetime(jpm["date_time"])
wells = pd.read_csv('Module 3/data/wells.csv')
wells["date_time"] = pd.to_datetime(wells["date_time"])
bac = pd.read_csv('Module 3/data/bac.csv')
bac["date_time"] = pd.to_datetime(bac["date_time"])
# endregion

## ---- START HERE ----

# Use merge_asof() to merge jpm (left table) and wells together on the date_time column, 
# where the rows with the nearest times are matched, and with suffixes=('', '_wells'). 
# Save to jpm_wells.
jpm_wells = ____

# Use merge_asof() to merge jpm_wells (left table) and bac together on the date_time 
# column, where the rows with the closest times are matched, and with 
# suffixes=('_jpm', '_bac'). 
# Save to jpm_wells_bac.
jpm_wells_bac = ____

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the close prices of close_jpm, close_wells, and close_bac from price_diffs.
price_diffs.plot(y=[____, ____, ____])
plt.show()

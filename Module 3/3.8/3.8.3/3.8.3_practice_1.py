"""
Concatenate and merge to find common songs
==========================================

The senior leadership of the streaming service is requesting your help again. You are given
the historical files for a popular playlist in the classical music genre in 2018 and 2019. 
Additionally, you are given a similar set of files for the most popular pop music genre 
playlist on the streaming service in 2018 and 2019. Your goal is to concatenate the 
respective files to make a large classical playlist table and overall popular music table. 
Then filter the classical music table using a semi join to return only the most popular 
classical music tracks.

The tables classic_18, classic_19, and pop_18, pop_19 have been loaded for you. 
Additionally, pandas has been loaded as pd.
"""

# region setup
import pandas as pd
classic_18 = pd.read_csv('Module 3/data/classic_18.csv')
classic_19 = pd.read_csv('Module 3/data/classic_19.csv')
pop_18 = pd.read_csv('Module 3/data/pop_18.csv')
pop_19 = pd.read_csv('Module 3/data/pop_19.csv')
# endregion

## ---- START HERE ----

# 1 
# Concatenate the classic_18 and classic_19 tables vertically where the index goes from 
# 0 to n-1, and save to classic_18_19.
classic_18_19 = ____

# Concatenate the pop_18 and pop_19 tables vertically where the index goes from 0 to n-1, 
# and save to pop_18_19.
pop_18_19 = ____

# 2
# With classic_18_19 on the left, merge it with pop_18_19 on tid using an inner join.
classic_pop = ____

# Use .isin() to filter classic_18_19 where tid is in classic_pop.
popular_classic = classic_18_19[classic_18_19[____].isin(____)]

# Print popular chart
print(popular_classic)

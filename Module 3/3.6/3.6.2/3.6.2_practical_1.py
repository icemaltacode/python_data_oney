"""
One-to-many merge
=================

A business may have one or multiple owners. In this exercise, you will continue to gain experience 
with one-to-many merges by merging a table of business owners, called biz_owners, to the licenses table. 
Recall from the video lesson, with a one-to-many relationship, a row in the left table may be repeated 
if it is related to multiple rows in the right table. In this lesson, you will explore this further by 
finding out what is the most common business owner title. (i.e., secretary, CEO, or vice president)

The licenses and biz_owners DataFrames are loaded for you.
"""

# region setup
import pandas as pd
licenses = pd.read_pickle('Module 3/data/licenses.p')
biz_owners = pd.read_pickle('Module 3/data/business_owners.p')
# endregion

## ---- START HERE ----

# Starting with the licenses table on the left, merge it to the biz_owners table on the column account,
#  and save the results to a variable named licenses_owners.
licenses_owners = ____

# Group licenses_owners by title and count the number of accounts for each title. Save the result as counted_df
counted_df = licenses_owners.groupby(____).agg({'account':'count'})

# Sort counted_df by the number of accounts in descending order, and save this as a variable named sorted_df.
sorted_df = counted_df.sort_values(____)

# Use the .head() method to print the first few rows of the sorted_df.
print(____)

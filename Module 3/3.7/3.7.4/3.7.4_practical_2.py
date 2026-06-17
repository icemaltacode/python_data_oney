"""
Do sequels earn more?
=====================

It is time to put together many of the aspects that you have learned in this chapter. 
In this exercise, you'll find out which movie sequels earned the most compared to the 
original movie. To answer this question, you will merge a modified version of the sequels 
and financials tables where their index is the movie ID. You will need to choose a merge 
type that will return all of the rows from the sequels table and not all the rows of 
financials table need to be included in the result. From there, you will join the resulting 
table to itself so that you can compare the revenue values of the original movie to the 
sequel. Next, you will calculate the difference between the two revenues and sort the 
resulting dataset.

The sequels and financials tables have been provided.
"""

# region setup
import pandas as pd
sequels = pd.read_pickle('Module 3/data/sequels.p').astype(object)
financials = pd.read_pickle('Module 3/data/financials.p')
# endregion

## ---- START HERE ----

# 1
# With the sequels table on the left, merge to it the financials table on index named id, 
# ensuring that all the rows from the sequels are returned and some rows from the other 
# table may not be returned, Save the results to sequels_fin.
sequels_fin = ____

# 2
# Merge the sequels_fin table to itself with an inner join, where the left and right 
# tables merge on sequel and id respectively with suffixes equal to ('_org','_seq'), 
# saving to orig_seq.
orig_seq = ____.merge(____, how=____, left_on=____, 
                             right_on=____, suffixes=____)

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# 3
# Select the title_org, title_seq, and diff columns of orig_seq and save this as titles_diff.
titles_diff = orig_seq[____]

# 4
# Sort by titles_diff by diff in descending order and print the first few rows.
print(titles_diff.sort_values(____).head())

"""
Performing a semi join
======================

Some of the tracks that have generated the most significant amount of revenue are from 
TV-shows or are other non-musical audio. You have been given a table of invoices that 
include top revenue-generating items. Additionally, you have a table of non-musical tracks 
from the streaming service. In this exercise, you'll use a semi join to find the top 
revenue-generating non-musical tracks.

The tables non_mus_tcks, top_invoices, and genres have been loaded for you.
"""

# region setup
import pandas as pd
non_mus_tcks = pd.read_csv('Module 3/data/non_mus_tcks.csv')
top_invoices = pd.read_csv('Module 3/data/top_invoices.csv')
genres = pd.read_csv('Module 3/data/genres.csv')
# endregion

## ---- START HERE ----

# Merge non_mus_tcks and top_invoices on tid using an inner join. 
# Save the result as tracks_invoices.
tracks_invoices = ____.merge(____)

# Use .isin() to subset the rows of non_mus_tcks where tid is in 
# the tid column of tracks_invoices. 
# Save the result as top_tracks.
top_tracks = _____[non_mus_tcks['tid'].isin(____)]

# Group top_tracks by gid and count the tid rows. Save the result to cnt_by_gid.
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':____})

# Merge cnt_by_gid with the genres table on gid and print the result.
print(____)

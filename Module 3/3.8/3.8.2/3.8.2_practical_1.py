"""
Concatenation basics
====================

You have been given a few tables of data with musical track info for different albums 
from the metal band, Metallica. The track info comes from their Ride The Lightning, 
Master Of Puppets, and St. Anger albums. Try various features of the .concat() method 
by concatenating the tables vertically together in different ways.

The tables tracks_master, tracks_ride, and tracks_st have loaded for you.
"""

# region setup
import pandas as pd
tracks_master = pd.read_csv('Module 3/data/tracks_master.csv')
tracks_ride = pd.read_csv('Module 3/data/tracks_ride.csv')
tracks_st = pd.read_csv('Module 3/data/tracks_st.csv')
# endregion

## ---- START HERE ----

# 1
# Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting sort to True.
tracks_from_albums = pd.concat(____,
                               sort=True)
print(tracks_from_albums)

# 2
# Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 0 to n-1.
tracks_from_albums = pd.concat(____,
                               ____,
                               sort=True)
print(tracks_from_albums)

# 3
# Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that are in all tables.
tracks_from_albums = pd.concat(____,
                               ____,
                               sort=True)
print(tracks_from_albums)

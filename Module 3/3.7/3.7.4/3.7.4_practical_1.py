"""
Index merge for movie ratings
=============================

To practice merging on indexes, you will merge movies and a table called ratings that 
holds info about movie ratings. Ensure that your merge returns all rows from the movies 
table, and only matching rows from the ratings table.

The movies and ratings tables have been loaded for you.
"""

# region setup
import pandas as pd
movies = pd.read_pickle('Module 3/data/movies.p')
ratings = pd.read_pickle('Module 3/data/ratings.p')
# endregion

## ---- START HERE ----

# Merge the movies and ratings tables on the id column, keeping all rows from the movies 
# table, and save the result as movies_ratings.
movies_ratings = ____

# Print the first few rows of movies_ratings
print(movies_ratings.head())

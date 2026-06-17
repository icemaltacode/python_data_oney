"""
Popular genres with right join
==============================

What are the genres of the most popular movies? To answer this question, you need to merge data from 
the movies and movie_to_genres tables. In a table called pop_movies, the top 10 most popular movies 
in the movies table have been selected. To ensure that you are analyzing all of the popular movies, 
merge it with the movie_to_genres table using a right join. To complete your analysis, count the 
number of different genres. Also, the two tables can be merged by the movie ID. However, in pop_movies 
that column is called id, and in movie_to_genres it's called movie_id.

The pop_movies and movie_to_genres tables have been loaded for you.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
movie_to_genres = pd.read_pickle('Module 3/data/movie_to_genres.p')
pop_movies = pd.read_csv('Module 3/data/pop_movies.csv')

# endregion

## ---- START HERE ----

# Merge movie_to_genres and pop_movies using a right join. Save the results as genres_movies.
genres_movies = ____.merge(____, how='____', 
                                      ____, 
                                      ____)

# Group genres_movies by genre and count the number of id values.
genre_count = genres_movies.groupby('____').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

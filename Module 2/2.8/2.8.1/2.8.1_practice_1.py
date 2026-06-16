"""
Switching between styles
========================

Selecting a style to use affects all of the visualizations that are created after this style is selected.

Here, you will practice plotting data in two different styles. The data you will use is the same weather 
data we used in the first lesson: you will have available to you the DataFrame seattle_weather and the 
DataFrame austin_weather, both with records of the average temperature in every month.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
seattle_weather = pd.read_csv('Module 2/data/seattle_weather.csv', index_col='DATE')
austin_weather = pd.read_csv('Module 2/data/austin_weather.csv', index_col='DATE')
# endregion

## ---- START HERE ----

# 1
# Select the 'ggplot' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.
____
____

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# 2
# Select the 'Solarize_Light2' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.
____
____
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

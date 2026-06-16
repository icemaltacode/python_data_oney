"""
Defining a function that plots time-series data
===============================================

Once you realize that a particular section of code that you have written is useful, it is a good idea to 
define a function that saves that section of code for you, rather than copying it to other parts of your 
program where you would like to use this code.

Here, we will define a function that takes inputs such as a time variable and some other variable and 
plots them as x and y inputs. Then, it sets the labels on the x- and y-axis and sets the colors of the 
y-axis label, the y-axis ticks and the tick labels.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)
climate_change = pd.read_csv("Module 2/data/climate_change.csv", parse_dates=["date"], index_col=["date"])
# endregion

## ---- START HERE ----

# Define a function called plot_timeseries that takes as input an Axes object (axes), data (x,y), 
# a string with the name of a color and strings for x- and y-axis labels.
def ____(axes, x, y, color, xlabel, ylabel):

  # Plot y as a function of in the color provided as the input color.
  axes.____(____, ____, color=____)

  # Set the x- and y-axis labels using the provided input xlabel and ylabel, 
  # setting the y-axis label color using color.
  
  # Set the x-axis label
  ____.____(____)

  # Set the y-axis label
  ____.____(____, color=____)

  # Set the y-axis tick parameters using the tick_params method of the Axes object, setting the colors key-word to color.
  ____.____('y', colors=____)
import matplotlib  # Imports the library, matplotlib, to configure a setting before graphing.
matplotlib.use("TkAgg")  # Configures the graphing library to work with the GUI library we're using.
import matplotlib.pyplot as plt  # Imports the plotting module from the graphing library.
import numpy as np  # Imports numpy for working with arrays.
import json  #


"""
This was a script that I used to graph points for a different project.
I copied the script to this project and changed it to work with this project.
"""

points = []  # Empty list of ordered pairs.

#               DISCARDED CODE
# x_points = []  # Empty list of x-points.
# y_points = []  # Empty list of y-points.
# for x, y in points:  # Appends all points from the list to their respective list of points.
#     x_points.append(x)
#     y_points.append(y)


# Takes the time string, 00:00, splits it into minutes and seconds, and returns an integer of total seconds.
def split_time(time: str):
    minstr = time[:2]  # Defines a variable, minstr, to hold the minutes part of the time string.
    secstr = time[3:]  # Defines a variable, secstr, to hold the seconds part of the time string.
    return (int(minstr) * 60) + int(secstr)  # Returns seconds from minutes plus the regular seconds.


# Takes JSON file name as an argument, gets the data from that JSON file, and then graphs it.
def graph_data(name: str):
    x_points = []  # Empty list of x-points.
    y_points = []  # Empty list of y-points.
    with open(name + '.json', 'r') as in_file:  # Opens the JSON file for reading
        logs = json.load(in_file)['intervals']  # Defines a variable, logs, as the list of data from the JSON file.
    for x, y in logs:  # Iterates through the list of points and appends them to their respective lists.
        x_points.append(split_time(x))
        y_points.append(y)
    # fig, ax = plt.subplots(1, 1)
    plt.scatter(np.asarray(x_points), np.asarray(y_points), c='black')  # Graphs the x and y points in a scatter plot.

    plt.show()  # Show the graph.

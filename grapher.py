import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import json


points = []  # Initial list of ordered pairs.
""""
Points is the list of points you want to average, each list item is an ordered pair (x, y).
Replace the empty list in the points variable with a list of tuples, which are ordered pairs.
ex: [(0,1), (2, 3), (4, 5)]
"""

# x_points = []  # Empty list of x-points.
# y_points = []  # Empty list of y-points.
# for x, y in points:  # Appends all points from the list to their respective list of points.
#     x_points.append(x)
#     y_points.append(y)


def split_time(time: str):
    minstr = time[:2]
    secstr = time[3:]
    return (int(minstr) * 60) + int(secstr)


def graph_data(name: str):
    x_points = []  # Empty list of x-points.
    y_points = []  # Empty list of y-points.
    with open(name + '.json', 'r') as in_file:
        logs = json.load(in_file)['intervals']
    for x, y in logs:  # Appends all points from the list to their respective list of points.
        x_points.append(split_time(x))
        y_points.append(y)
    # fig, ax = plt.subplots(1, 1)
    plt.scatter(np.asarray(x_points), np.asarray(y_points), c='black')

    plt.show()

#!venv/bin/python

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from Graph import Graph
from Movie import Movie
from Actor import Actor
import json
from analysis import mainprocess

#age vs income plot
graph = mainprocess()
graph.setconnect()

x = []
y = []

for i in range(len(graph.actorVertex)):
    if graph.actorVertex[i].age != -1:
        x.append(graph.actorVertex[i].age)
        y.append(graph.actorVertex[i].value)

#calculate correlation
print(np.corrcoef(x, y))

plt.scatter(x, y)
plt.show()
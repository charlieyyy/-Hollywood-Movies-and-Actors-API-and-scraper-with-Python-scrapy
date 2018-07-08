#!venv/bin/python

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from Graph import Graph
from Movie import Movie
from Actor import Actor
import json
from analysis import mainprocess

# create hub actor bar chart
graph = mainprocess()
graph.setconnect()
idlist = []
connection = []
for i in range(len(graph.actorVertex)):
    idlist.append(graph.actorVertex[i].index)
    connection.append(graph.actorVertex[i].connection)

print(idlist)
print(connection)

plt.bar(idlist,connection,align='center') # A bar chart

plt.xlabel('Connection')
plt.ylabel('Actor')
plt.title('Hub Actor Analysis')

plt.show()


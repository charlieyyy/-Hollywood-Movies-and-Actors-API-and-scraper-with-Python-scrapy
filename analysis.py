import json
import re
from Movie import Movie
from Actor import Actor
from Graph import Graph
from operator import itemgetter


#the main function to convert json file to graph structure
def mainprocess():
    json_data = open('242data.json')
    data = json.load(json_data)

    actordict = data[0]
    moviedict = data[1]
    actorkeys = list(actordict.keys())
    moviekeys = list(moviedict.keys())

    graph = Graph()

    for i in range(len(moviekeys)):
            m = createmovie(moviedict[moviekeys[i]], i)
            graph.add_movievertex(m)

    for j in range(len(actorkeys)):

            a = createactor(actordict[actorkeys[j]], j)
            graph.add_actorvertex(a)

    return graph

#create movie objects from data file
def createmovie(dict, index):
    value = dict['box_office']
    year = dict['year']
    mitem = Movie(dict['name'], value, dict['actors'], index, year)
    return mitem

#create actor objects from data file
def createactor(dict,index):
    age = dict['age']
    year = 2018 - age
    aitem = Actor(dict['name'], age, dict['movies'], index, dict['total_gross'], year, 0)
    return aitem

# who is the hub actor?
graph = mainprocess()
print(graph.hubactor())

# which age group makes the most money?
print(graph.richest_group())
mydict = graph.richest_group()
print(sorted(mydict.items(), key = itemgetter(1), reverse = True))


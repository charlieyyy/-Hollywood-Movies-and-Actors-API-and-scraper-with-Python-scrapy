import json
import re
from Movie import Movie
from Actor import Actor
from Graph import Graph


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

            a = createactor(actordict[actorkeys[i]], i)
            graph.add_actorvertex(a)

    return graph

#create movie objects from data file
def createmovie(dict, index):
    value = dict['box_office']
    year = dict['year']
    mitem = Movie(dict['name'], value, dict['actors'], index, year)
    return mitem

#working the grossing value to make it integer
def getnum(grossing):
    if grossing is not None:
        ret = re.sub("[^0-9]", "", grossing)
        ret = convertStr(ret)
        if 'million' in grossing:
            ret = ret * 1000000
        if 'billion' in grossing:
            ret = ret * 1000000000
        return ret
    else:
        return None

#string manipulation on movieyear
def getYear(s):
    if s is not None:
        if (')' not in s) and (s!= '\n'):
            return s[-4:]
        else:
            return s[-5:-1]
    else:
        return None

#create actor objects from data file
def createactor(dict,index):
    age = dict['age']
    year = 2018 - age
    aitem = Actor(dict['name'], age, dict['movies'], index, dict['total_gross'], year)
    return aitem

#string manipulation on actoryear
def actorYear(list):
    for i in range(len(list)):
        if '19' in list[i]:
            a=list[i][-5:]
            a.replace(" ", "")
            return a

#a useful helper function to convert string to int
def convertStr(s):
    """Convert string to either int or float."""
    if s is None:
        return None

    try:
        ret = int(s)
    except ValueError:
        ret = None
    return ret

mainprocess()
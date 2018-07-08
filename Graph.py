import numpy as np
import json
from Movie import Movie
from Actor import Actor


class Graph:

    def __init__(self):
        self.actorVertex = []
        self.movieVertex = []
        self.adjmatrix = None
        self.actorbyage = None
        self.actorbyvalue = None


    def add_actorvertex(self, actor):
        if actor not in self.actorVertex:
            self.actorVertex.append(actor)


    def add_movievertex(self, movie):
        if movie not in self.movieVertex:
            self.movieVertex.append(movie)


    #adjMatrix creation: rows represent actor and cols represent movies
    def create_adjmatrix(self):
        if (len(self.actorVertex) >= 1) and (len(self.movieVertex) >= 1):
            self.adjmatrix = np.zeros((len(self.actorVertex), len(self.movieVertex)))
            for i in range(len(self.actorVertex)):
                for j in range(len(self.actorVertex[i].movieList)):
                    self.adjmatrix[i, self.actorVertex[i].movieList[j]] = self.actorVertex[i].movieList[j].value + self.actorVertex[i].age
        return self.adjmatrix

    #query: Find how much a movie has grossed
    def grossing(self, name):
        for i in range(len(self.movieVertex)):
            if self.movieVertex[i].name == name:
                return self.movieVertex[i].value

    #List which movies an actor has worked in
    def workedfilms(self, name):
        for i in range(len(self.actorVertex)):
            if self.actorVertex[i].name == name:
                return self.actorVertex[i].movieList

    #List which actors worked in a movie
    def cast(self, name):
        for i in range(len(self.movieVertex)):
            if self.movieVertex[i].name == name:
                return self.movieVertex[i].castList

    def top_helper(self):
        a = []
        for i in range(len(self.actorVertex)):
            a.append(self.actorVertex[i])
        a.sort(key=lambda actor: actor.value, reverse = True)
        self.actorbyvalue = a

    #List the top X actors with the most total grossing value
    def top(self, num):
        self.top_helper()
        count = 0
        ret = []
        while count < num:
            ret.append(self.actorbyvalue[count].name)
            count += 1
        return ret


    def old_helper(self):
        a = []
        for i in range(len(self.actorVertex)):
            a.append(self.actorVertex[i])
        a.sort(key=lambda actor: actor.age, reverse = True)
        self.actorbyage = a

    #List the oldest X actors
    def old(self, num):
        self.old_helper()
        count = 0
        ret = []
        while count < num:
            ret.append(self.actorbyage[count].name)
            count += 1
        return ret

    #List all the movies for a given year
    def movie_givenyear(self, year):
        ret = []
        for i in range(len(self.movieVertex)):
            if self.movieVertex[i].year == year:
                ret.append(self.movieVertex[i].name)
        return ret

    #List all the actors for a given year
    def actor_givenyear(self, year):
        ret = []
        for i in range(len(self.actorVertex)):
            if self.actorVertex[i].year == year:
                ret.append(self.actorVertex[i].name)
        return ret

    #https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
    # a serializer method:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def actor_value(self):
        for i in range(len(self.actorVertex)):
            value = 0
            for j in range(len(self.actorVertex[i].movieList)):
                name = self.actorVertex[i].movieList[j]
                for k in range(len(self.movieVertex)):
                    if (name ==self.movieVertex[k].name) and (self.movieVertex[k].value is not None):
                        value+=self.movieVertex[k].value
            self.actorVertex[i].value = value

    def setconnect(self):
        for i in range(len(self.actorVertex)):
            cvalue = 0
            for j in range(len(self.actorVertex[i].movieList)):
                name = self.actorVertex[i].movieList[j]
                for k in range(len(self.movieVertex)):
                    if (name == self.movieVertex[k].name) and (self.movieVertex[k].castList is not None):
                        cvalue += len(self.movieVertex[k].castList)
            self.actorVertex[i].connection = cvalue

    def hubactor(self):
        self.setconnect()

        a = []
        for i in range(len(self.actorVertex)):
            a.append(self.actorVertex[i])
        a.sort(key=lambda actor: actor.connection, reverse=True)
        return a[0].name

    def richest_group(self):
        age20, age30, age40, age50, age60, age70, age80, age90 = (0,0,0,0,0,0,0,0)
        for i in range(len(self.actorVertex)):
            if(self.actorVertex[i].age < 30 ) and (self.actorVertex[i].age >= 20 ):
                age20 += self.actorVertex[i].value
            if (self.actorVertex[i].age < 40) and (self.actorVertex[i].age >= 30):
                age30 += self.actorVertex[i].value
            if (self.actorVertex[i].age < 50) and (self.actorVertex[i].age >= 40):
                age40 += self.actorVertex[i].value
            if (self.actorVertex[i].age < 60) and (self.actorVertex[i].age >= 50):
                age50 += self.actorVertex[i].value
            if (self.actorVertex[i].age < 70) and (self.actorVertex[i].age >= 60):
                age60 += self.actorVertex[i].value
            if (self.actorVertex[i].age < 80) and (self.actorVertex[i].age >= 70):
                age70 += self.actorVertex[i].value
            if (self.actorVertex[i].age < 90) and (self.actorVertex[i].age >= 80):
                age80 += self.actorVertex[i].value
            if (self.actorVertex[i].age < 100) and (self.actorVertex[i].age >= 90):
                age90 += self.actorVertex[i].value

        grouplist = {}
        grouplist['age20'] = age20
        grouplist['age30'] = age30
        grouplist['age40'] = age40
        grouplist['age50'] = age50
        grouplist['age60'] = age60
        grouplist['age70'] = age70
        grouplist['age80'] = age80
        grouplist['age90'] = age90

        return grouplist

from Graph import Graph
from Movie import Movie
from Actor import Actor
import json
from analysis import mainprocess

graph = mainprocess()
print(graph.hubactor())
#graph.actor_value()
#print(graph.toJSON())


name = input("What's your name? ")
print("Nice to meet you " + name + "!")

# query: Find how much a movie has grossed
movie = input("Find how much a movie has grossed (type a name of a movie)")
print("The box office of  " + str(movie) + " is ")
print(graph.grossing(str(movie)))

#List which movies an actor has worked in
actor = input("List which movies an actor has worked in (type a name of the actor)")
print("Movies in which " + str(actor) + " is part of include")
print(graph.workedfilms(str(actor)))

#List which actors worked in a movie
mactor = input("List which actors worked in a movie (type a name of the movie )")
print("The cast of " + str(mactor) + " are: ")
print(graph.cast(str(mactor)))

#List the top X actors with the most total grossing value
top = input("List the top X actors with the most total grossing value(type a number)")
print("The richest " + str(top) + " actors are: ")
print(graph.top(int(top)))

#List the oldest X actors
old = input("List the oldest X actors (type a number)")
print("The oldest " + str(old) + " actors are: ")
print(graph.old(int(old)))

#List all the movies for a given year
myear = input("List all the movies for a given year (type a year)")
print("Movies in " + str(myear) + " including: ")
print(graph.movie_givenyear(str(myear)))

#List all the actors for a given year
ayear = input("List all the actors for a given year (type a year)")
print("Actors born " + str(ayear) + " including: ")
print(graph.actor_givenyear(str(ayear)))
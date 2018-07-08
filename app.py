#!venv/bin/python

from flask import Flask, jsonify, request
from analysis import mainprocess
from Movie import Movie
from Actor import Actor
import json

app = Flask(__name__)

graph = mainprocess()
graph.hubactor()

@app.route('/actors', methods=['GET'])
def get_actor():
    name = request.args.get('name',default='*',type=str)
    age = request.args.get('age',default=1,type=int)
    value = request.args.get('value',default=1,type=int)
    year = request.args.get('year',default=1,type=int)
    connection = request.args.get('connection',default=1,type=int)

    list = []
    for i in range(len(graph.actorVertex)):
        if name in graph.actorVertex[i].name:
            list.append(graph.actorVertex[i].name)
        if age == graph.actorVertex[i].age:
            list.append(graph.actorVertex[i].name)
        if value == graph.actorVertex[i].value:
            list.append(graph.actorVertex[i].name)
        if year == graph.actorVertex[i].year:
            list.append(graph.actorVertex[i].name)
        if connection == graph.actorVertex[i].connection:
            list.append(graph.actorVertex[i].name)
    list1 = Remove(list)

    list2 =[]
    for i in range(len(graph.actorVertex)):
        list2.append(graph.actorVertex[i].name)

    ret = Diff(list2,list1)

    return jsonify(ret)

@app.route('/actors/<name>', methods=['GET'])
def get_actorbyname(name):
    actor = {}
    for i in range(len(graph.actorVertex)):
        if graph.actorVertex[i].name == name:
            ret = ret_actor(actor, graph.actorVertex[i])
            return jsonify(ret)


@app.route('/movies', methods=['GET'])
def get_movie():
    name = request.args.get('name',default='*',type=str)
    value = request.args.get('value',default=1,type=int)
    year = request.args.get('year',default=1,type=int)

    list = []
    for i in range(len(graph.movieVertex)):
        if name in graph.movieVertex[i].name:
            list.append(graph.movieVertex[i].name)
        if value == graph.movieVertex[i].value:
            list.append(graph.movieVertex[i].name)
        if year == graph.movieVertex[i].year:
            list.append(graph.movieVertex[i].name)
    list1 = Remove(list)

    list2 =[]
    for i in range(len(graph.movieVertex)):
        list2.append(graph.movieVertex[i].name)

    ret = Diff(list2,list1)

    return jsonify(ret)

@app.route('/movies/<name>', methods=['GET'])
def get_moviebyname(name):
    movie = {}
    for i in range(len(graph.movieVertex)):
        if graph.movieVertex[i].name == name:
            ret = ret_movie(movie, graph.movieVertex[i])
            return jsonify(ret)

@app.route('/actors/<actorname>', methods=['PUT'])
def update_actor(actorname):
        data = request.get_json()

        if 'age' in data:
            age = data['age']
            for i in range(len(graph.actorVertex)):
                if graph.actorVertex[i].name == name:
                    graph.actorVertex[i].age = age
        if 'value' in data:
            value = data['value']
            for i in range(len(graph.actorVertex)):
                if graph.actorVertex[i].name == name:
                    graph.actorVertex[i].valye = value
        if 'year' in data:
            year = data['year']
            for i in range(len(graph.actorVertex)):
                if graph.actorVertex[i].name == name:
                    graph.actorVertex[i].year = year

@app.route('/actors', methods=['POST'])
def add_actor():
    data = request.get_json()
    actor = Actor(data['name'],-1,[],-1,-1,-1,-1)
    graph.add_actorvertex(actor)

@app.route('/actors', methods=['DELETE'])
def delete_actor():
    data = request.get_json()
    name = data['name']
    for i in range(len(graph.actorVertex)):
        if graph.actorVertex[i].name == name:
            del graph.actorVertex[i]

@app.route('/movies/<moviename>', methods=['PUT'])
def update_movie(moviename):
    data = request.get_json()

    if 'value' in data:
        value = data['value']
        for i in range(len(graph.movieVertex)):
            if graph.movieVertex[i].name == name:
                graph.movieVertex[i].valye = value
    if 'year' in data:
        year = data['year']
        for i in range(len(graph.movieVertex)):
            if graph.movieVertex[i].name == name:
                graph.movieVertex[i].year = year

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    movie = Movie(data['name'],0,[],-1,-1)
    graph.add_movievertex(movie)

@app.route('/movies', methods=['DELETE'])
def delete_movie():
    data = request.get_json()
    name = data['name']
    for i in range(len(graph.movieVertex)):
        if graph.movieVertex[i].name == name:
            del graph.movieVertex[i]


def ret_actor(actor, dict):
    actor['name'] = dict.name
    actor['age'] = dict.age
    actor['movieList'] = dict.movieList,
    actor['index'] =dict.index,
    actor['value'] = dict.value,
    actor['year'] = dict.year,
    actor['connection'] = dict.connection
    return actor

def ret_movie(movie, dict):
    movie['name'] = dict.name
    movie['index'] =dict.index,
    movie['value'] = dict.value,
    movie['year'] = dict.year,
    movie['castlist'] = dict.castList
    return movie

def Diff(li1, li2):
    return list(set(li1) - set(li2))

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


if __name__ == '__main__':
    app.run(debug=True)
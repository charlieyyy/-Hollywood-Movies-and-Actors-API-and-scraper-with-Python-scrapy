from unittest import TestCase
from Movie import Movie
from Actor import Actor
from Graph import Graph

actorone = Actor("Leland Orser", 60, ['A', 'B', 'C'], 0, 1000000, 1958, 1000)
actortwo = Actor("Charlie Yang", 25, ['A', 'B', 'C', 'D'], 1, 8000000, 1993, 100)
actorthree = Actor("Snoop Dog", 40, ['A'], 2, 500000, 1978, 500000)

movie_a = Movie('A', 500000, ["Leland Orser", "Charlie Yang", "Snoop Dog"], 0, 2010)
movie_b = Movie('B', 200000, ["Leland Orser", "Charlie Yang"], 1, 2014)
movie_c = Movie('C', 300000, ["Leland Orser", "Charlie Yang"], 2, 2014)
movie_d = Movie('D', 7000000, ["Charlie Yang"], 3, 2016)

graph = Graph()

graph.add_actorvertex(actorone)
graph.add_actorvertex(actortwo)
graph.add_actorvertex(actorthree)

graph.add_movievertex(movie_a)
graph.add_movievertex(movie_b)
graph.add_movievertex(movie_c)
graph.add_movievertex(movie_d)


class TestGraph(TestCase):

    def test_add_actorvertex(self):
        self.assertTrue("actor in right position", graph.actorVertex[actorone.index] == actorone)
        self.assertTrue("actor in right position", graph.actorVertex[actortwo.index] == actortwo)
        self.assertTrue("actor in right position", graph.actorVertex[actorthree.index] == actorthree)

    def test_add_movievertex(self):
        self.assertTrue("movie in right position", graph.movieVertex[movie_a.index] == movie_a)
        self.assertTrue("movie in right position", graph.movieVertex[movie_b.index] == movie_b)
        self.assertTrue("movie in right position", graph.movieVertex[movie_c.index] == movie_c)

    def test_grossing(self):
        self.assertTrue("return right amount", graph.grossing('D') == 7000000)
        self.assertTrue("return right amount", graph.grossing('A') == 500000)

    def test_workedfilms(self):
        self.assertTrue("return right films", graph.workedfilms("Charlie Yang") == ['A', 'B', 'C', 'D'])

    def test_cast(self):
        self.assertTrue("return right actors", graph.cast('A') == ["Leland Orser", "Charlie Yang", "Snoop Dog"])

    def test_top(self):
        graph.top_helper()
        print(graph.top(2))
        self.assertTrue("the highest two is right", graph.old(2) == ["Charlie Yang", "Leland Orser"])

    def test_old(self):
        graph.old_helper()
        print(graph.old(2))
        self.assertTrue("the oldest two is right", graph.old(2) == ["Leland Orser", "Snoop Dog"])

    def test_movie_givenyear(self):
        print(graph.movie_givenyear(2014))
        self.assertTrue("right movie in 2014", graph.movie_givenyear(2014) == ['B', 'C'])
        print(graph.movie_givenyear(2016))
        self.assertTrue("right movie in 2016", graph.movie_givenyear(2016) == ['D'])

    def test_actor_givenyear(self):
        print(graph.actor_givenyear(1993))
        self.assertTrue("return charlie yang", graph.actor_givenyear(1993) == ['Charlie Yang'])
        print(graph.actor_givenyear(1978))
        self.assertTrue("return snoop dog", graph.actor_givenyear(1978) == ['Snoop Dog'])

    def test_hubactor(self):
        self.assertTrue("return snoop dog", graph.hubactor() == ['Snoop Dog'])


    def test_richest_group(self):
        self.assertTrue("right dict", graph.richest_group() ==
                                {'age20': 8000000, 'age30': 0, 'age40': 500000, 'age50': 0, 'age60': 1000000, 'age70': 0, 'age80': 0,
                                'age90': 0}  )


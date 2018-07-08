class Actor:

    def __init__(self, name, age, movieList,index, value, year, connection):

        self.name = name
        self.age = age
        self.movieList = movieList
        self.index = index
        self.value = value
        self.year = year
        self.connection= connection

    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'movieList': self.movieList,
            'index': self.index,
            'value': self.value,
            'year': self.year,
            'connection':self.connection
        }





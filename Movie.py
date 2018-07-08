class Movie:

    def __init__(self, name, value, castList, index , year):

        self.name = name
        self.value = value
        self.castList = castList
        self.index = index
        self.year = year

    def serialize(self):
        return {
            'name': self.name,
            'value': self.value,
            'castlist': self.castList,
            'index': self.index,
            'year': self.year
        }


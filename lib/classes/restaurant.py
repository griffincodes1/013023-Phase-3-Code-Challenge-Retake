class Restaurant:
    all = []

    def __init__(self, name):
        if type(name) == str:
            self._name = name
            self.all.append(self)
        else:
            raise Exception("The restaurant name must be a string")

        self.reviews = []
        self.customers = []


    def get_name(self):
        return self._name

    name = property(get_name)

    def average_star_rating(self):
        return sum([review.rating for review in self.reviews]) / len(self.reviews)


    @classmethod
    def get_all_restaurants(cls):
        return cls.all

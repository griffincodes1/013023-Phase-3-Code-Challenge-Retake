class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = []
        self._full_name = self.get_first_name() + ' ' + self.get_last_name()


    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        if type(first_name) == str and ( len(first_name) > 0 and len(first_name) < 26 ):
            self._first_name = first_name
        else:
            raise Exception("Your first name must contain between 1 and 25 letters inclusiv")

    first_name = property(get_first_name, set_first_name)


    def get_last_name(self):
        return self._last_name


    def set_last_name(self, last_name):
        if type(last_name) == str and ( len(last_name) > 0 and len(last_name) < 26 ):
            self._last_name = last_name
        else:
            raise Exception("Your last name must be a string and contain between 1 and 25 letters inclusive")

    last_name = property(get_last_name,set_last_name)


    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_num_reviews(self):
        return len(self.reviews)

    def create_review(self, restaurant, rating):
        from classes.review import Review
        Review(self, restaurant, rating)

        
class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id, self.description, self.rating))

class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))

    def add_review(self, review):
        self.reviews.append(review)


b1 = Book(1, 'Knjiga 1', 'Darko')
print(b1)

b1.add_review(Review(100, 'Ok', 3))
b1.add_review(Review(1, 'Very Good', 4))
print(b1)
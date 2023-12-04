# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Special Class Methods


# Challenge:
# Given a class that represents a Book with various properties such
# as title, author, pagecount, etc:


# 5) Successfully execute the sample code provided below.

from enum import Enum


class Book():

    
    def __init__(self, title, author, pages, cover, antique, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover = cover
        self.antique = antique
        self.price = price

    # TODO: Implement the str and repr functions
    
    def __str__(self):
        return f"{self.title} by {self.author}: {self.pages}, {self.cover}, {self.price}"

    def __repr__(self):
        return f"<Book:{self.title}:{self.author}:{self.pages}:{self.cover}:{self.antique}:{self.price}"

    # TODO: Implement the adjustedprice attribute
    def __getattr__(self, attr):
        if attr == "adjustedprice":
            price = self.price
            if self.antique:
               price = price + 10.00
            if self.cover == cover_type.PAPERBACK:
                price = price - 2.00
            return price

        else:
            raise AttributeError("Invalid attribute")


    # TODO: Implement comparisons <, >, <=, >=
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __ge__(self, other):
        return self.pages >= other.pages 
    
    def __lt__(self, other):
        return self.pages < other.pages 
    
    def __le__(self, other):
        return self.pages <= other.pages 


# TODO: Implement the Hard/Paperback Enum
class cover_type(Enum):
    HARD = 0
    PAPERBACK = 1


books = [
    Book("War and Peace", "Leo Tolstoy", 1225, cover_type.HARD, True, 29.95),
    Book("Brave New World", "Aldous Huxley", 311, cover_type.PAPERBACK, True, 32.50),
    Book("Crime and Punishment", "Fyodor Dostoevsky", 492, cover_type.HARD, False, 19.75),
    Book("Moby Dick", "Herman Melville", 427, cover_type.PAPERBACK, True, 22.95),
    Book("A Christmas Carol", "Charles Dickens", 66, cover_type.HARD, False, 31.95),
    Book("Animal Farm", "George Orwell", 130, cover_type.PAPERBACK, False, 26.95),
    Book("Farenheit 451", "Ray Bradbury", 256, cover_type.HARD, True, 28.95),
    Book("Jane Eyre", "Charlotte Bronte", 536, cover_type.PAPERBACK, False, 34.95)
]

# TEST CODE

# 1 - test the str and repr functions
print("-------------")
print(str(books[0]))
print(str(books[3]))
print(str(books[5]))
print()
print(repr(books[0]))
print(repr(books[3]))
print(repr(books[5]))
print("-------------")

# 2 - test the "adjustedprice" computed attribute
for book in books:
    print(f"{book.title}: {book.adjustedprice:.2f}")
print("-------------")
print()

# 3 - compare on pagecount
print(books[1] > books[2])
print(books[4] < books[6])
print(books[7] >= books[0])
print(books[3] <= books[4])

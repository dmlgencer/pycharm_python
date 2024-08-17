

from oopConcept.Book import Book
class Author(Book):
    def __init__(self, name, birthday, bookName, bookYear):
        super().__init__(name,birthday)
        self.bookName = bookName
        self.bookYear = bookYear

    def showInfo(self):
        return f"Author: {self.name}, Birthday: {self.birthday}, bookName: {self.bookName}, bookYear: {self.bookYear}"

Author = Author("Stefan Zweig", "1881", "Dünün Dünyası", "1942")
print(Author.showInfo())


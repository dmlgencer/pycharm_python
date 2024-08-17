

class Book:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def showInfo(self):
        return f"Book: {self.name} {self.birthday}"

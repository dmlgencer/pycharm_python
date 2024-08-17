

class Person:
    def __init__(self, name, university):
        self.name = name
        self.university = university
        print("Person Created")


class Student(Person):
    def __init__(self, name, university):
        Person.__init__(self, name, university)
        print("Student Created")

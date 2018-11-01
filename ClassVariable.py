class Person:
    'This is the optional class documentation string, which can be accessed by ClassName.__doc__'
    # Class variables
    totalNumPerson = 0

    def __init__(self, name):
        self.name = name
        Person.totalNumPerson += 1

    def PrintName(self):
        print(self.name)

    def printTotalNumPerson(self):
        print(Person.totalNumPerson)
        return Person.totalNumPerson



p1 = Person("Rex")
p2 = Person("Alex")
p3 = Person("WW")
p1.printTotalNumPerson()
print(Person.__doc__)
p3.printTotalNumPerson()

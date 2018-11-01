class Person:

    population = 0

    def __init__(self, name):
        # public variable
        self.name = name
        # private variable
        self.__manufacturerOrder = Person.population + 1

        Person.population += 1

    def printDetails(self):
        print(self.name)
        print(self.__manufacturerOrder)



Rex = Person('Rex')
Alex = Person('Alex')
# Access public variable, will succeed
print(Rex.name)

Rex.printDetails()
Alex.printDetails()

# Access private variable, will fail
print(Rex.__manufacturerOrder)

# Actually, the private accessibility method is just a rule, not the limitation of compiler.
# Its fact is to change name of private name like
# __variable or __function() to _ClassName__variable or _ClassName__function().
# So we can’t access them because of wrong names.

# Access private variable using the special syntax

print(Rex._Person__manufacturerOrder)
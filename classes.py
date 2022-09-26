#

print ()

class Animal:

    def __init__(self, name, size, animal_type):

        x = 10
        
        self.name = name
        self.size = size
        self.animal_type = animal_type

    def animal(self):
        print ("A", self.name, "is a", self.size, "animal. It is a(n)", self.animal_type, "\n")

animal1 = Animal("lion", "large", "mammal.")
animal1.animal()

animal2 = Animal("frog", "small", "amphibian.")
animal2.animal()

#

class Integer:

    x = 100

my_integer = Integer()

print (my_integer.x)

print ()
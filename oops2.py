#Method Overriding Examples same methods inherite but different behiviour

class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("make a sound")
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says woof")
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says meow")

animal1 = Animal("Tiger")
animal2 = Dog("charlii")
animal3 = Cat("ranii")

animal1.make_sound()
animal2.make_sound()
animal3.make_sound()


#Polymorphisom--> same method different behaviour depends on which object call it
class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("make a sound")
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says woof")
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says meow")
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says tweet")
class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} says grrrrr")

Addnames = [Animal("animals"),Cat("Queen"),Dog("Raja"),Bird("Chinni"),Lion("simhaa")]

for i in Addnames:
    i.make_sound()

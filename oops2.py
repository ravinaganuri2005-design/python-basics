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

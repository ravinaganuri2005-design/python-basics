class car:   
    def __init__(self,brand,color):  #__init__ is  constructor — runs when object is created
        self.brand = brand   #attributes
        self.color = color
    def drive(self):  # drive is a method (behaviour)
        print(f"{self.color} {self.brand} is driving")

# Create objects from the class
car1 = car("Honda","Red")
car2 = car("suzuki","Blue")

car1.drive()
car2.drive()

        

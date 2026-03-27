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



#Just another example of using class and objects methods 
class phone:
    def __init__(self,brand,price,battery):
        self.brand = brand
        self.price = price
        self.battery = battery
    def show_info(self):
        print(f"I buy the {self.brand} and price {self.price} battery pickup {self.battery}")

phone1 =phone ("iphone","180000","Good")
phone2 = phone("samasang","98000","Very Good")

phone1.show_info()
phone2.show_info()


#examples of creating objects and class atributes
class Dog:
    def __init__(self,bark,food):
        self.bark = bark
        self.food = food
    def walk(self):
        print(f"my dog eating {self.food} my dog barking like{self.bark}")
        
dog1 = Dog("boww","leg peice")
dog2 = Dog("grrrrrrrrrr","rotiii")

dog1.walk()
dog2.walk()


#Encapsulation example-> private

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit (self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited{amount}")
        else:
            print("invalid amount")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
    def get_balance(self):
        return self.__balance
acc = BankAccount(10000)

acc.deposit(5000)          # Deposited ₹5000
acc.withdraw(3000)         # Withdrawn ₹3000
print(acc.get_balance())   # 12000

# Try to break it
acc.deposit(-500)          # Invalid amount!
acc.withdraw(99999)        # Not enough balance!

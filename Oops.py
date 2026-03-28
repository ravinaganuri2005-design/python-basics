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


#with encapsulation 

class BankAccs:
    def __init__(self,balancing):
        self.__balancing = balancing

    def deposits(self,amounts):
        if amounts > 0:
            self.__balancing += amounts
            print(f"Added{amounts}")
        else:
            print("Invalid amount")
    def get_balancing(self):
        print(f"balancing is {self.__balancing}")
accs = BankAccs(8000)
accs.deposits(4000)
accs.get_balancing()

#same above example with explanation
class BankAccs:                          # ← class name        — NOT private
    def __init__(self, balancing):       # ← method name       — NOT private
        self.__balancing = balancing     # ← THIS variable     — 🔒 PRIVATE

    def deposits(self, amounts):         # ← method name       — NOT private
        if amounts > 0:                  # ← logic             — NOT private
            self.__balancing += amounts  # ← using the private variable (allowed — inside class)

    def get_balancing(self):             # ← method name       — NOT private
        print(f"balancing is {self.__balancing}")  # ← reading private variable (allowed)


#INHERITANCE PROBLEM
class vehical:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} is starting")
    def stop(self):
        print(f"{self.brand} is stoping")
class car(vehical):
    def honk(self):
        print(f"{self.brand} Beep beep!") 

class Bike(vehical):
    def whiele(self):
        print(f"{self.brand} Doing a wheliee") 

# car object 
car1 = car("BMW")    
car1.start()
car1.stop()
car1.honk()

#Bike object
Bike1 = Bike("XL")
Bike1.start()
Bike1.stop()
Bike1.whiele()

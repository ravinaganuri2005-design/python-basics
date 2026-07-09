 #GETTER AND SETTER WITH SOME EXAMPLES
class rectangel:
    def __init__(self,width,height):
       self.width = width
        self.height =height
    
    @property   #getter
    def width(self):
        return self._width
    
    @width.setter   #setter
    def width(self,values):
        if values <=0:
            print("width must be positive")
        else:
            self._width = values
    
    @property  #getter
    def height(self):
        return self._height
    
    @height.setter  #setter
    def height(self,values):
        if values <= 0:
            print("hieght must be positive")
        else: 
         self._height = values
     
    @property  #ONLY READ THE VALUE NO SETTER
    def area(self):
        return self._width * self.height
    
    @property # ONLY GETTER NO SETTER
    def perimater(self):
          return 2 * (self._width + self._height)
    
r = rectangel(4,5)
    
print(r.width)# READ
print(r.height)
print(r.area)
print(r.perimater)

r.width =23  # CHANGE THE VALUE
print(r.width)



class student:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    @property
    def age(self): #Getter
        print("someone can read your info")
        return self._age
    
    @age.setter  #Setter
    def age(self,value):
        print("someone change your information")
        if value < 5 or value > 100:
            print("change the age between  5 to 100")
        else:
            self._age = value
s = student("Ravi",22)
print(s.age)  # try to read the info
s.age = 25   # set new value to age
print(s.age)  # print the new value
s.age = 200
print(s.age)r.height = -77  # NO CHANGE BECOUSE IT IS NAGETIVE
print(r.height)



#ABSTRACT CLASS
#Abstract class = a template that forces every subclass
#  to implement certain methods, and can't be used to create objects on its own.


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card ")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Cash ")


# ---- Use it ----
payments = [CreditCard(), PayPal(), Cash()]

for p in payments:
    p.pay(100)

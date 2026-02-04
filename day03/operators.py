# #Logical Operators

X = int(input("enter first number"))
Y = int(input("enter second number"))

print("both numbers are greater than 10",X > 10 and Y >10)
print("one numbers are less than 5", X < 5 or Y < 5)
print(" the first number is greater than second",not (X > Y))

# #comparison operator

x = int(input ("enter your age:"))
if x >= 20:
    print(" you are an adult")
elif x > 20:
    print(" your are less than 20")
elif x== 15:
    print("your in the 7th standard")

#  #membership operator
y = input("enter the string")
print("contains a", 'a ' in y)
print("contains python", 'python' not in y)


my_list = [1,2,3,4,5,6]
my_string = ("Ravi")
print(3 in my_list)
print(6 not in my_list)
print("v" in my_string)
print("z" not in my_string)

# #Bitwise operator

a = int(input("enter the number") )
b = int(input("enter the second number") )
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("~b =", ~b)

# # bitwise operator works            truth table

a = 6 #binary value is 110        1  1  0
b = 4 # binary value is 100       1  0  0 
print(a & b)  #output 100         1  0  0  

     
a = 6                           # 1 1 0 
b = 4                           # 1 0 0
print(a | b ) # output is 110     1 1 0

''1. Arithmetic Operators'''


#write a program to add two numbers
a = 32
b = 45
c = a + b
print(c)

#Take two numbers from the user and print their sum, difference, product, and quotient.
x = int(input("enter first number "))
y = int(input("enter second number"))
print(x + y)
print(x -y)
print(x * y)
print(x / y)
print(x // y)

#Find the remainder when a number is divided by 7.
x = 13
y =7
z = x % y
print(z)

#Calculate the area of a circle using πr².
r = 5
area = 3.14 * r * r
print("area of circle is ",area)

# #Swap two numbers using a temporary variable.'''
a = 32
b = 12
temp = a 
a = b
b = temp
print(a,b)

# #Take a number and check if it is divisible by 5 using %.
a = int(input("enter a number"))
if a % 5 == 0:
    print("it is possible to division:")
else:
    print("its not possible")

# #Convert seconds into minutes using // and %.
seconds = int(input("enter a numbers"))
minutes = seconds // 60
remaining = seconds % 60
print("minutes ",minutes)
print("seconds ",seconds)

#Take two numbers and print which one is greater.
x = int(input("enter first number "))
y = int(input("enter second number "))
if x > y:
    print("x is greater")
else:
    print("y is greater")

#Check if two strings are equal.
a = "ravi"
b = "Ravi"
if a.lower()==b.lower():
    print('both strings are equal')
else:
    print("its not same")

#Take a number and check if it is between 10 and 50.
#Check if the entered character is a vowel.

num = int(input('enter a number '))
if num >= 10 and num <= 50:
    print("number is more than 10 and less than 50 ")
else:
    print("num is not between 10 to 50")

char = input("Enter a character: ").lower()  # convert to lowercase
if char in ['a', 'e', 'i', 'o', 'u']:
    print("The character is a vowel")
else:
    print("The character is not a vowel")

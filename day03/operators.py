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

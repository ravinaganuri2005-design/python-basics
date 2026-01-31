'''Beginner Level  Python Strings
Create a string and print it.
Take a string input from the user and print it.
Find the length of a string.
Access:
First character
Last character
Print each character of a string using a loop.
Convert a string to:
Uppercase
Lowercase
Check whether a string contains a specific character.
Count how many times a character appears in a string.
Reverse a string.
Check whether a string is empty or not.'''

#1
x = "Ravi Naganuri"
print(type(x))
#2
# y = input("enter a string ")
# print(y)
#3
print(len(x))
#4
z = "naganuri"
print(z[0],z[-1])
#5
each_char = "BiggBoss"
for char in each_char:
    print(char)
#6
a = each_char.upper()
b = each_char.lower()
print(a,b)
#7
spec_char = "python"
ch = "a"
if ch in spec_char:
    print("this char found")
else:
    print("this char not found")
#8
repeat_char = 'ravi naganuri'
print(repeat_char.count("a"))
#9
revers_string = "Gangstar"
print(revers_string[::-1])
#10
j = input("enter a string: ")
if len(j)==0:
    print("this string is empty ")
else:
    print("this is not empty")

#input and output
#
#f is known as formatted string
#concanite both string
# print(f"{boy_name} loves {girl_name}.")

name=" Ravi, Naganuri"

print(name.upper())
print(name.lower())
print(name.replace("Naganuri","Patil"))
print(name.strip())# remove the spaces
print(name.capitalize())#first character capital
print(name.center(30))# align the string
print(name.casefold())#its similar to lower but this is more characters converted into lower case
print(name.count("a"))# count the number of same characters
print(name.encode())#encodes the string using the specified encoding
print(name.endswith("u"))#if the string ends with the specified value its true
name1 = "H\te\tl\tl\to\t" # \t means tab space
print(name1)
print(name1.expandtabs(2))# set the tab size of a string
print(name1.expandtabs(4))
print(name1.expandtabs(7))
print(name1.expandtabs(10))

print(name.find("Naganuri"))#find the number of characters

text="my name is{fname}, I am {age}"
print(text.format(fname=" john", age= 21))# it is used to insert the value in string (placeholder)

name2 = "Ravi2005"
print(name2.isalnum())#it specified all the string is alpha numaric
print(name2.isalpha())#it specified the strings is alphabets or not
print(name2.isascii())
print(name2.isdecimal())#strings is decimal 
print(name2.isidentifier())# it consider only alphabets and underscore, numbers

name3 = "239495"
print(name3.isdigit())

just = "  "
print(just.isspace())

title = "Hi My Name Is Ravi"
print(title.istitle())# its must start with the alpha, other wise it is false

eat = "I could eat banana"
print(eat.partition("eat"))# it divide the string part wise

#string concatination

first_name="Vinod"
last_name="Doddalinganavar"
print(first_name + " Annappa "+ last_name)


say_love = " I Love You "
print(say_love *30)

a = "hello word"
print(a[0])

age = 36
txt = "My name is John, I am {age}"
print(txt)


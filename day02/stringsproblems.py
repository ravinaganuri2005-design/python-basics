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


'''Intermediate Level – String Operations & Logic
Check if a string is a palindrome.
Count:
Vowels
Consonants
Count number of:
Words
Digits
Spaces
Replace a word in a string.
Remove all spaces from a string.
Find the first and last occurrence of a character.
Check if two strings are anagrams.'''

#1
pali = "ravi"
rev = ""
for char in pali:
    rev = char + rev
    if pali == rev:
        print ("it is palindrom")
    else:
        print("its not palindrom")

s = "madam"
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#2
latter = "programming"
vowels = 0
consonants = 0
for char in latter:
    if char in "aeiou":
        vowels += 1
    else:
        consonants +=1 
print("total vowels is ",vowels)
print("total consonants is ",consonants)

#3
s = "add31234   "
word = 0
spaces = 0
digits = 0
for char in s:
    if char.isalpha():
        word += 1
    elif char.isdigit():
        digits +=1
    elif char.isspace():
        spaces += 1
print("word is ",word)
print("digits is ",digits)
print("spaces is ",spaces)

#4
p = "I love Python"
old_word = "Python"
new_word = "Java"

result = ""
world = ""

for ch in p + " ":          # extra space to process last word
    if ch != " ":
        world += ch
    else:
        if world == old_word:
            result += new_word + " "
        else:
            result += world + " "
        world = ""
print(result.strip())

#5
m = " P ra  jwal  "
result =""
for char in m:
    if char !=" ":
        result += char
print(result)


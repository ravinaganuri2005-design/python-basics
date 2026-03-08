#function to get sum of two numbers

# declare the function
def get_sum(number1,number2):
    return(number1 + number2 )

#invocation or calling the function
sum = get_sum(20,30)
print("the sum of two numbers",sum)

sum2 = get_sum(1.3 , 2.5)
print("the sum of two float numbers",sum2)

#swap the numbers between two numbers

def swap(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp
    return item1, item2

# def swapSimple(item1, item2):    
#     return item2, item1

def invoke_swap():
    number1 = 10
    number2 = 20

    print(f"Before swapping: Value of number1 = {number1} and number2 = {number2}")
    number1, number2 = swap(number1, number2)

    # number1, number2 = swapSimple(number1, number2)
    print(f"After swaping: Value of number1 = {number1} and number2 = {number2}")
invoke_swap()


#write a function find the numbers is even or odd

def even_odd_number(n)->bool:
    if (n % 2 == 0):
        return True
    else:
        return False
result = even_odd_number(5)
if result:
    print("even number")
else:
    print("odd number")


#write the function isdigit is number return true if it is digit
def Isdigit(number):
    isInteger = True
    for eachcharacter in number:
        if(eachcharacter >='0' and eachcharacter <= '9'):
            continue
        else:
            isInteger = False
            break
    return isInteger
ans = Isdigit('1234a')

if ans:
    print("all are digits")
else:
    print("its not a digit")

#write a function simple greeting  accept your name and age as a input

def simpleGreeting():
    name = input("enter your name: ")
    age = input("enter your age: ")
    print(f"My name is {name}")
    print(f"i am {age}year older")
simpleGreeting()

# write the function to find the length of string

#simple method 
a = "abc"
b = len(a)
print(b)

#in logic building method

def string_len(s)->int:
    count = 0  
    for character in s:
        count = count + 1
    return count

input = "abdce"
print(f"input is {input} -> and their length is {string_len(input)}")

input2 = ""
print(f"input is {input2} and their length is {string_len(input2)}")


# write a function to count the vowels in string

def count_vowels(x):
    counter = 0
    for char in x:
        if (char == 'a' or
            char == 'e' or
            char == 'i' or
            char == 'o' or
            char == 'u' or
            char == 'A' or 
            char == 'E' or
            char == 'I' or
            char == 'O' or
            char == 'U'):
            counter = counter + 1

    return counter
input = "ravi"
vowel_count = count_vowels(input)
print(f"in the {input} is have a {(vowel_count)}vowels" )

# it is another method to get a count the vowels in the string

def count_vowels(x):
    counter = 0
    for char in x:
        if char in "aeiouAEIOU":
            counter += 1
    return counter

text = "abcde"
vowel_count = count_vowels(text)
print(f"In the string '{text}', there are {vowel_count} vowels.")


# write a function to reverse a string

def reverse(string):
    reverse_string = ""
    for i in range(len(string)-1,-1,-1):
        reverse_string =  reverse_string + string[i]
    return reverse_string
string = "ravi"
a = reverse(string)
print("reverse string is",a)



#write a function to check string is pallindrom

def isPalindrom(string:str)->bool:
    leftindex = 0
    rightindex = len(string) -1
    result = True

    while (leftindex < rightindex):
        if string [leftindex] != string[rightindex]:
            result = False 
        break
    leftindex = leftindex + 1
    rightindex = rightindex - 1
    return result

input = "mam"
input1 = "malayalam"
input3 = "sir"

result = isPalindrom(input3)
if result:
    print("string is a palindrom")
else:
    print("string is not palindrom")


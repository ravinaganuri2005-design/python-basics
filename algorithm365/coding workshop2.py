#fizzbuzz
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizbuz")
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz(15)
#count the character more than one time apear
def count_char(s, char):
    count = 0
    for letter in s:
        if letter == char:
            count = count + 1
    return count

s = str(input("enter a string: "))
char = str(input("enter a char: "))
print(count_char(s,char))


#find the second largest number
def second_largest(numbers):
    maxfirst = 0
    maxsecond = 0
    for i in numbers:
        if i > maxfirst:
            maxsecond = maxfirst  
            maxfirst = i
        elif i > maxsecond:
            maxsecond = i         
    return maxsecond
result =[1,2,3,3,5]
print(second_largest(result))

# Remove zeros from a list

numbers = [1, 0, 3, 0, 5, 0, 7, 8]
result = [n for n in numbers if n != 0]
print(result)

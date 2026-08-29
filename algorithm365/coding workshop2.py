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

# find the power of 2 
def power_of_two(number):
    if number <= 0:
        return False
    while number != 1:
        if (number % 2 != 0):
            return False
        number = number // 2
    return True
value = 6
print(power_of_two(value))


#binary search 
def binary_search():

    arr = [5, 10, 15, 20, 25, 30, 35]
    target = 25
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print("Found at index:", mid)
            return
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print("Not Found")
binary_search()



#armstrong number

class solution:
    def isarm_strong_number(self,n):
        duplicate = n
        digits = len(str(n))
        total = 0
        while n >0:
            digit = n % 10
            total = total + digit ** digits
            n = n // 10
        if total ==duplicate:
            return True
        else:
            return False
obj = solution()
print(obj.isarm_strong_number(152))

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



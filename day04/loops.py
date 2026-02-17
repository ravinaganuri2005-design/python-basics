text = "rabi"
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Reversed string:", reverse)

text = "hello"
reversed_text = ''.join(reversed(text))
print(reversed_text)  # Output: "olleh"

squares=[number ** 2 for number in range(6)]
print(squares)

names=["Ravi","vinod","abhi","prashant"]
for name in names:
    print(name)

# breaking the loop
for index in range(10):
    if index == 5:
        print("breaking the loop")
        break
    print(index)

names=["Ravi","vinod","abhi","prashant"]
for names in names:
    print(names)
    if(names == "abhi"):
        continue
    print(names)

num=[1,2,4,5,6,7,7,8,9,]
for num in num:
    print(num)
    if(num==6):
        print("6 num is found")
        break
    else:
        print("6 num is not found")


num = 1
while num <= 20:
    if num % 5 ==0:
        num += 1
        continue
    print(num)
    num += 1

while True:
    password = input ("enter the password:")
    if password == "python123":
        print("correct password")
        break
    else:
        print("error password")


#multipication problem
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

#Count how many elements are in a list.
numbers = [1, 2, 3, 4, 5]
count = 0
for num in numbers:
    count += 1

print(count)

#check palindrome or not

num = int(input("Enter number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#print numbers 1 to 20
i = 0
while i<=10:
    print(i,end = " ")
    i += 1
#print numbers with step of 2
for i in range(1,20,2):
    print(i)

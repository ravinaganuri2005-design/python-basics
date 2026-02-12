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


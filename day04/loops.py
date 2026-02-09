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

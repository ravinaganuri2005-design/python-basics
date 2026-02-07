text = "rabi"
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Reversed string:", reverse)

text = "hello"
reversed_text = ''.join(reversed(text))
print(reversed_text)  # Output: "olleh"

#first non repeating character
text = "aabbcde"
frequency ={}
for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i]=1
for i in text:     #which character first apears 1 time 
    if frequency[i]==1:
        print(i)
        break

#print the first twice repeating character

s = "abcdeef"
frequencys ={}
for i in s:
    if i in frequencys:
        frequencys[i] +=1
    else:
        frequencys[i] = 1
for i in s:
    if frequencys[i]>1:
        print(i)
        break

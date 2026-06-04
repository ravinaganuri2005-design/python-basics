# A good way to improve logic is to describe the algorithm in plain English before coding:
"I will assume the first element is the largest. Then I will compare"
" every element with the current largest. If I find a bigger "
"one, I will make it the new largest."

#find the largest of in list
list = [1,2,3,48,15,6]
max = list[0]
for i in list:
    if i > max:
        max = i
print(max)

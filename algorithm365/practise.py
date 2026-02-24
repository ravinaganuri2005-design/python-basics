#Find the number as user input using function
#definition
def len_search(numbers,key):
    for num in numbers:
        if num==key:
            print("number is found")
            return
          
        #declaration
  
    print("number is not found")
numbers=[10,20,30,40,50,60]
key=int(input("enter a number you want: "))
#calling or invoke
len_search(numbers,key)

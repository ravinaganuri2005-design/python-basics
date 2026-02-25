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


# print the edges stars
def print_edge_stars(gridsize):
    for  row in range(1, gridsize+1 ,1):
        for column in range(1, gridsize +1, 1):
            if row == 1 or row == gridsize or column == 1 or column == gridsize:
                print("*" ,end=" ")
            else:
                print(" ",end=" ")
        print()    
print_edge_stars(5) 


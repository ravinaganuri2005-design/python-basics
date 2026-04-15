#print the stars
def print_star(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (j<=i): # For print *
                print("*", end=" ")
            else: #For space
                print(" ",end=" ")
        print() #next line
n = int(input("enter a number "))
print_star(n)

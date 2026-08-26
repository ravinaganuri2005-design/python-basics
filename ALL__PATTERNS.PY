#Pattern 1

print("Pattern 1")
class solution:
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                 print("*",end ="")
            print()
obj = solution()
obj.pattern1(5)

OUTPUT:Pattern 1
*****
*****
*****
*****
*****


#Pattern 2
print("Pattern 2")
class Solution2:
    def pattern2(self,n2):
        for i in range(n2):
            for j in range(i +1):
                print("*", end = "")
            print()
obj = Solution2()
obj.pattern2(5)

OUTPUT:Pattern 2
*
**
***
****
*****


#Pattern 3
print("pattern 3")
class Solution:
    def pattern3(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print(j+1, end ="")
            print()
obj = Solution()
obj.pattern3(5)

OUTPUT:pattern 3
1
12
123
1234
12345



#Pattern 4
print("pattern 4")
class Solution:
    def pattern4(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print(i,end ="")
            print()
obj = Solution()
obj.pattern4(5)

output:
pattern 4
1
22
333
4444
55555

#Pattern 5
print("pattern 5")
class Solution:
    def pattern5(self, n):
        for i in range(1,n+1):
            for j in range(n - i+1):
                print("*",end ="")
            print()
obj = Solution()
obj.pattern5(5)

output:
pattern 5
*****
****
***
**
*

#pattern 6
print("Pattern 6")
class solution:
    def pattern6(self,n):
        for i in range(1,n+1):
            for j in range(1,n-i+2):
                print(j, end = "")
            print()
obj = solution()
obj.pattern6(5)

Output:
12345
1234
123
12
1



# Pattern 7
print("Pattern 7")
class solution:
    def pattern7(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end ="")
            for j in range(2*i+1):
                print("*",end ="")
            for j in range(n-i-1):
                print(" ",end ="")
            print()
obj = solution()
obj.pattern7(5)

output:
    *    
   ***   
  *****  
 ******* 
*********

#Pattern 8
print("pattern 8")
class solution:
    def pattern8(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end ="")
            for j in range(2*n -(2*i+1)):
                print("*",end ="")
            for j in range(i):
                print(" ",end ="")
            print()
obj = solution()
obj.pattern8(5)

output:
*********
 ******* 
  *****  
   ***   
    *  

#Pattern 9
print("Pattern 9")
class solution:
    def pattern7(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end ="")
            for j in range(2*i+1):
                print("*",end ="")
            for j in range(n-i-1):
                print(" ",end ="")
            print()
    def pattern8(self,n):
            for i in range(n):
                for j in range(i):
                    print(" ",end ="")
                for j in range(2*n -(2*i+1)):
                    print("*",end ="")
                for j in range(i):
                    print(" ",end ="")
                print()
obj = solution()
obj.pattern7(5)
obj.pattern8(5)

output:
Pattern 9
    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    *    

#pattern 10 
print("pattern 10")
class solution3:
    def pattern10(self,n):
        for i in range(2*n-1):
            stars = i +1
            if (i >= n): 
                stars = 2*n-i-1
            for j in range(0,stars):
                print("*",end ="")
            print()
obj=solution3()
obj.pattern10(5)

output:
pattern 10
*
**
***
****
*****
****
***
**
*

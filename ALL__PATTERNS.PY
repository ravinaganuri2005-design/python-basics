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

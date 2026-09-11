#fibonacci problem
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        first = self.fib(n-1)
        second = self.fib(n-2)
        result = first + second

        return result
obj = Solution()
print(obj.fib(4))

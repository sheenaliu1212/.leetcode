#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        i = self.fib(n-1)
        j = self.fib(n-2)
        return i + j
# @lc code=end


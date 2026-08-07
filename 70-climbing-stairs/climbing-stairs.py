class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i  - 2]
        return ways[n]
"""
3 stairs
Option 1:
1 step + 1 step + 1 step
Option 2:
1 step + 2 steps
Option 3:
2 steps + 1 step

Subproblem
ways(i) = number of distinct ways to reach i.
Base cases
ways(1) = 1 (a normal step)
ways(2) = 2 (a jump)

Formula that connects
ways(i) = ways(i - 1) = ways(i -2) 


Bottom-up approach
start from base cases and build a table forward

""" 
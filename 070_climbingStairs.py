class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        n1, n2 = 1, 2
        for i in range( 3, n + 1):
            n2, n1 = n1 + n2 , n2
        return n2

n = 4
x = Solution()
print(x.climbStairs(n))
"""
70. Climbing Stairs
Easy https://youtu.be/Y0lT9Fck7qI
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
Accepted
1,808,020
Submissions
3,504,978
"""
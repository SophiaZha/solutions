from typing import List

class Solution:
    # the shorted and easiest solution below - official
    def change(self, amount: int, coins: List[int]) -> int:
        result = [0] * ( amount + 1 )
        result[0] = 1
        for coin in coins:
            for i in range( coin, amount + 1):
                result[i] = result[i] + result[i - coin];
        return result[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        # Time: O(n*m)
        # Memory: O(n*m)
        cache = {}
        def dfs(i, curSum):
            if i == len(coins):
                return 0
            if curSum > amount:
                return 0
            if curSum == amount:
                return 1
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            cache[(i, curSum)] = dfs(i, curSum + coins[i]) + dfs(i + 1, curSum)
            return cache[(i, curSum)]
        return dfs(0, 0)

    def change2(self, amount: int, coins: List[int]) -> int:
        # Time: O(n*m)
        # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

    def change3(self, amount: int, coins: List[int]) -> int:
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
"""
518. Coin Change II
Medium
Share
You are given an integer array coins representing coins of different denominations and an integer amount representing a 
total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination 
of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
Accepted
352,805
Submissions
592,444
"""
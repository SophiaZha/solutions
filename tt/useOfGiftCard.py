# https://leetcode.com/problems/coin-change-ii/solution/
# https://github.com/neetcode-gh/leetcode/blob/main/python/0322-coin-change.py
# https://www.youtube.com/watch?v=Mjy4hd2xgrs

from typing import List

class Solution:
    def getFewestNumberOfCards(self, giftcardValue: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in giftcardValue:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

    def getCombinationOfGiftCards(self, numberOfCards: int, amount: int) -> int:
        if amount < 10 or amount % 10 != 0:
            return -1
        amount /= 10
        giftCardValue = [1, 3, 5]
        dp = [0] * (amount + 1)
        dp[1] = 1

        for a in range(1, amount + 1):
            for c in giftCardValue:
                if a - c > 0:
                    dp[a] =  dp[a - c]
                elif a - c == 0:
                    dp[a] += 1
        return dp[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        # DYNAMIC PROGRAMMING
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

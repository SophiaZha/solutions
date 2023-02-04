# https://leetcode.com/problems/coin-change-ii/solution/
# https://github.com/neetcode-gh/leetcode/blob/main/python/0322-coin-change.py
# https://www.youtube.com/watch?v=Mjy4hd2xgrs
# find the total combination for the exact number of cards used to reach the total.
class Solution:
    def change(self, amount: int,  numberOfCards: int) -> int:
        if amount < 10 or amount % 10 != 0:
            return -1
        amount /= 10
        amount = int(amount)
        coins = [5, 3, 1]
        dp = [[[0,[]] for j in range(amount + 1)] for k in range(3)]
        for i in range(3):
            dp[i][0][0] = 1
            dp[i][0][1] = [0]  # inititla card, using 0 card
        c = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                if dp[c][x - coin][0] > 0:
                    dp[c][x][0] += dp[c][x - coin][0]  # number of combinations
                    dp[c][x][1] = [ i + 1 for i in dp[c][x - coin][1]]  # number of cards in a list
                    # try the below line to replace the above line for better storage usage
                    # dp[c][x][1] = [ i + 1 for i in dp[c][x - coin][1] if i <= (numberOfCards - (amount -x)//coin )]
                if c > 0:
                    if dp[c-1][x][0] > 0:
                        dp[c][x][0] += dp[c-1][x][0] # number of combinations
                        dp[c][x][1].extend(dp[c-1][x][1])  #
            c += 1
        ret = dp[2][amount][1].count(numberOfCards)
        return -1 if ret == 0 else ret

so = Solution()
totalAmount = 80
numberOfCards = 4
print(so.change( totalAmount, numberOfCards))

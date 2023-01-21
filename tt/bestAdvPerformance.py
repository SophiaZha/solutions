# https://leetcode.com/discuss/study-guide/1152328/01-Knapsack-Problem-and-Dynamic-Programming
from typing import List

class Solution:
    def getBestAdvPerformance(self, budget : int , adv_type: List[List[int]] ) -> int:
        dp =  [[0 for i in range( budget + 1 )] for j in range(len(adv_type) + 1)]
        for a in range(len(adv_type)):
            for d in range(budget + 1):
                if adv_type[a][0] <= d :
                    dp[ a + 1][d] = max(dp[a][d], dp[a][d- adv_type[a][0]] + adv_type[a][1])
                else:
                    dp[a +1][d] = dp[a][d]
        return dp[len(adv_type)][budget]


so = Solution()
n = 10
adv_type = [[10, 3000],[5,2000], [3,1000], [2,800],[1,200]]  # $, user_quantity
adv_type = [[3,1000], [2,800],[1,200], [10, 3000],[5,2000]]  # $, user_quantity


n = 100
adv_type = [[1000, 3000],[500,2000], [200,1000], [100,800],[50,200]]  # $, user_quantity
print(so.getBestAdvPerformance(n, adv_type))










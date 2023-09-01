from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) -3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0],cost[1])

    def minCostClimbingStairsL(self, cost: List[int]) -> int:
        n = len(cost)
        paid = [0] * n
        paid[n - 1] = cost[n - 1]
        paid[n - 2] = min(cost[n - 2], paid[n - 1] + cost[n - 2])
        for i in range(len(cost) - 3, -1, -1):
            paid[i] = min(cost[i] + paid[i + 2], paid[i + 1] + cost[i])
        return min(paid[0], paid[1])

cost = [10, 15, 20]
sol = Solution()
print(sol.minCostClimbingStairs(cost))
cost = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs(cost))

"""
746. Min Cost Climbing Stairs
Easy
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
Accepted
625,976
Submissions
1,012,557
"""

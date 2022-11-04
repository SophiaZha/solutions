from typing import List


class Solution:  # L
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.getMax(nums[1:]), self.getMax(nums[:-1]))

    def getMax(self, nums: List[int]) -> int:
        n1, n2 = 0, 0

        for n in nums:
            n2, n1 = max(n2, n + n1), n2

        return n2
#############
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def simple_rob(nums, i, j):
            rob, not_rob = 0, 0
            for idx in range(i, j):
                num = nums[idx]
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(simple_rob(nums, 1, n), simple_rob(nums, 0, n - 1))


"""
213. House Robber II
Medium

6867

105

Add to List

Share
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
Accepted
483,601
Submissions
1,192,012
"""
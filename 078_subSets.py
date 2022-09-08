from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp_res = []

        def dfs(i):
            if (i == len(nums)):
                res.append(tmp_res.copy())
                return
            else:
                tmp_res.append(nums[i])
                dfs(i + 1)
                tmp_res.pop()
                dfs(i + 1)

        dfs(0)
        return res


mynum = [1, 2, 3]
x = Solution()
print(x.subsets(mynum))

""" 
78. Subsets
Medium
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
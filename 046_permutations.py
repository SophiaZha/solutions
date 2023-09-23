from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res

    def permuteO(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            print("backtrack curr "+ str(curr), " ", end = " ")
            if len(curr) == len(nums):
                ans.append(curr[:])
                print("finishing curr " + str(curr), " ", end=" ")
                return
            for num in nums:
                print("num in nums is: ", num, " ", end = "")
                if num not in curr:
                    print(" appending : ", num)
                    curr.append(num)
                    backtrack(curr)
                    print("poping : ", num)
                    curr.pop()

        ans = []
        backtrack([])
        return ans
nums = [1,2,3]
s = Solution()
# print(s.permute(nums))
# nums = [1,2,3]
print(s.permuteO(nums))
#[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
#[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
46. Permutations   https://www.youtube.com/watch?v=s7AvT7cGdSo
Medium
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
Accepted
1,317,142
Submissions
backtrack curr []   num is:  1   appending :  1
backtrack curr [1]  num is:  1  
                    num is:  2   appending :  2
                                                   backtrack curr [1, 2]   
                                                   num is:  1  num is:  2  num is:  3   appending :  3
                                                   backtrack curr [1, 2, 3]   finishing curr [1, 2, 3]   poping :  3
                                 poping :  2
                    num is:  3   appending :  3
                                                   backtrack curr [1, 3]  num is:  1  num is:  2   appending :  2
                                                   backtrack curr [1, 3, 2]   finishing curr [1, 3, 2]   poping :  2
                                                   num is:  3  
                                poping :  3
                                poping :  1
                   
                   num is:  2   appending :  2
backtrack curr [2]   num is:  1   appending :  1
backtrack curr [2, 1]   num is:  1  num is:  2  num is:  3   appending :  3
backtrack curr [2, 1, 3]   finishing curr [2, 1, 3]   poping :  3
poping :  1
num is:  2  num is:  3   appending :  3
backtrack curr [2, 3]   num is:  1   appending :  1
backtrack curr [2, 3, 1]   finishing curr [2, 3, 1]   poping :  1
num is:  2  num is:  3  poping :  3
poping :  2
num is:  3   appending :  3
backtrack curr [3]   num is:  1   appending :  1
backtrack curr [3, 1]   num is:  1  num is:  2   appending :  2
backtrack curr [3, 1, 2]   finishing curr [3, 1, 2]   poping :  2
num is:  3  poping :  1
num is:  2   appending :  2
backtrack curr [3, 2]   num is:  1   appending :  1
backtrack curr [3, 2, 1]   finishing curr [3, 2, 1]   poping :  1
num is:  2  num is:  3  poping :  2
num is:  3  poping :  3
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Process finished with exit code 0
"""
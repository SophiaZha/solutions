class Solution(object):
    def productBySkip(self, nums, k):  # not correct solution actually
        ans = 1
        for i in range(len(nums)):
            if (i != k):
                ans *= nums[i]
        return ans

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = list(range(len(nums)))
        totalnum = 1
        for val in nums:
            totalnum *= val

        for i in range(len(nums)):
            if (nums[i] != 0):
                ans[i] = totalnum / nums[i]
            else:
                ans[i] = self.productBySkip(nums, i)

        return ans
"""
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Accepted
1,322,411
Submissions
2,051,780
"""
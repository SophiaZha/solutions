from typing import List


class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = -2**32
        for i in range(len(nums)):
            if curSum < 0:
                if nums[i] >= 0 :
                    curSum = nums[i]
                else:
                    curSum = max( curSum, nums[i])
            else:
                curSum += nums[i]
            maxSum = max(maxSum, curSum)

        return maxSum

    #nice and clean
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                    nums[i] += nums[i-1]
        return max(nums)

so = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(so.maxSubArray(nums))
nums = [1]
print(so.maxSubArray(nums))
nums = [5,4,-1,7,8]
print(so.maxSubArray(nums))
nums = [-1, -2]
print(so.maxSubArray(nums))
nums = [-2, -1]
print(so.maxSubArray(nums))

"""
53. Maximum Subarray
Medium
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Accepted
2,659,425
Submissions
5,333,988
"""

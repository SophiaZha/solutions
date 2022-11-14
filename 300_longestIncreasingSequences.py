from bisect import bisect_left
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:  #Time complexity: O(N2)O(N2)
        lis = [1] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)

    def lengthOfLISO(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:  #Time complexity: O(N2)O(N2)
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)

    def lengthOfLIS3(self, nums: List[int]) -> int:   #N*LogN Time Complexity Binary Search
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)


"""
300. Longest Increasing Subsequence
Medium

15102

269

Add to List

Share
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

Accepted
1,054,164
Submissions
2,049,475
"""
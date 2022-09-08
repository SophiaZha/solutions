from typing import List


class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
            numset = set(nums)
            length, longest = 0, 0
            for curNumber in numset:
                if (curNumber -1) not in numset:
                    length = 1
                    while (curNumber + length) in numset:
                        length += 1
                    longest = max(longest, length)
            return longest

nums = [100,4,200,1,3,2]
so = Solution()
print(so.longestConsecutive(nums))


"""
128. Longest Consecutive Sequence
Medium

12830

531

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
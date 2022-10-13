from typing import List


class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:  #not meet requirment, but it works
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def findDuplicate2(self, nums: List[int]) -> int:
        numset = set()
        for n in nums:
            if n in numset:
                return n
            else:
                numset.add(n)

    def findDuplicate3(self, nums: List[int]) -> int:
        for n in nums:
            if nums[abs(n) - 1] < 0:
                return abs(n)
            else:
                nums[abs(n) - 1] = -1 * nums[abs(n) - 1]

    def findDuplicate41(self, nums: List[int]) -> int:

        def store(nums: List[int], cur: int) -> int:
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)

        return store(nums, 0)

    def findDuplicate42(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]

    def findDuplicate5(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1

        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1

        return duplicate

    def findDuplicate6(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n + 1):
                # If bit is set in number (i) then add 1 to base_count
                if i & mask:
                    base_count += 1

                # If bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1

            # If the current bit is more frequently set in nums than it is in
            # the range [1, 2, ..., n] then it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask

        return duplicate

    def findDuplicate7(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

"""
287. Find the Duplicate Number
Medium

16134

2101

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
Accepted
980,575
Submissions
1,660,084
"""
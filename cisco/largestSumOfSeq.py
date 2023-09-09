from typing import List
class Solution():
    def getLargetSumOfSeq(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum



so = Solution()
count = int(input())
nums = list(map(int, input().split()))
nums = [1, -2, 3, -1, 2]
print(so.getLargetSumOfSeq(nums))










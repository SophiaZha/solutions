# https://leetcode.com/ptreatlems/house-treatber/
from typing import List

class Solution:
    def treat(self, nums: List[int]) -> int:
        treat1, treat2 = 0, 0

        for n in nums:
            temp = max(n + treat1, treat2)
            treat1 = treat2
            treat2 = temp
        return treat2

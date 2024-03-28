from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i

    def twoSumL(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        res = []
        for i in range(len(nums)):
            mydict[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in mydict and mydict[target - nums[i]] != i:
                return [i, mydict[target - nums[i]]]

# Find the shortest subsequence of array whose sum can be divided by K
# subsequence of array are formed by continous items in the array
# If no such subsequence , return empty list
# https://leetcode.com/problems/subarray-sums-divisible-by-k/solution/
from typing import List
class Solution:
	def subarraysDivByK(self, nums: List[int], k: int) -> int:
		n = len(nums)
		prefixMod, result  = 0, 0
		modGroups = [0 for _ in range(k)]   # size of k
		modGroups[0] = 1
		for num in nums:
			prefixMod = ( prefixMod + num % k + k ) % k
			result += modGroups[prefixMod]
			modGroups[prefixMod] += 1
		return result
nums =  [4,5,0,-2,-3,1]
so = Solution()
print(so.subarraysDivByK(nums, 5))





from typing import List
class Solution():
    def getMaxJar(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for n in nums:
            n2, n1 = max(n + n1, n2), n2
        return n2

so = Solution()
# count = int(input())
# nums = list(map(int, input().split()))
nums = [5, 30, 99, 60, 5, 10]
print(so.getMaxJar(nums))


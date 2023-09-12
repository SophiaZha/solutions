import collections
from typing import List
import numpy as np

class Solution:
    def getLargetPackets(self, points : List[List[int]]) -> int:
        xNum, yNum = collections.defaultdict(int), collections.defaultdict(int)
        for x, y in points:
            xNum[x] +=1
            yNum[y] +=1
        return max( max(xNum.values()), max(yNum.values()))

    def getLargetPacketsL(self, points) -> int:
        xNum, yNum = collections.defaultdict(int), collections.defaultdict(int)
        for x, y in points:
            xNum[x] += 1
            yNum[y] += 1
        return max( max(xNum.values()), max(yNum.values()))

so = Solution()
# n = int(input())
# px = list(map(int, input().split()))
# n = int(input())
# py = list(map(int, input().split()))
# pxy = np.transpose([px, py])
pxy = [[2,2], [3,2], [2,6], [4,5], [2,8]]
pxy = [[2,2], [3,2], [2,6], [4,5], [2,8], [1,2], [2,90], [2, 9]]

# txy = zip(px, py)
# txy = [[2,2], [3,2], [2,6], [4,5], [2,8], [1,2], [2,90], [2,9]]
print(so.getLargetPackets(pxy))
# print(so.getLargetPacketsL(txy))
# 5
# 2 3 2 4 2
# 5
# 2 2 6 5 8
# user Counter
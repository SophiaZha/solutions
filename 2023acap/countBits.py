#1 0 0 1 0 1-> 37
#1 2 3 4 5 6
# how many 1
# 1 to k, location starting from 1 -> and list of them
# 161 -># 3 1 3 8
from collections import Counter
class Solution:
    def getBinStr(self, dec: int):
        binStr = str(bin(dec)) #'0b10100001'
        counting = Counter(binStr)
        print(counting["1"])
        for i in range(2, len(binStr)):
            if binStr[i] == "1":
                print(i -1)

so = Solution()
print(so.getBinStr(161))


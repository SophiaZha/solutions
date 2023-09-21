class Solution:
    def getSubStr(self, instr:str, k:int) ->str:
        l, r, N, oneCounts, res = 0, k - 1, len(instr), 0, ""
        minL, minStr = N, "1"*k
        for i in range(k -1, N):
            oneCounts = instr[l:r+1].count("1")
            if oneCounts == k:
                curStr = instr[l:r+1]
                if r+1-l <= minL and curStr <= minStr:
                    minL = r + 1 -l
                    minStr = curStr
                    minStr = minStr.lstrip("0")
                    leadingZeroStripped = len(curStr) - len(minStr)
                    l += leadingZeroStripped
                    minL -= leadingZeroStripped
                if r < N -1 :
                    r += 1
                    l += 1
            else:
                r += 1
        return minStr
so = Solution()
print(so.getSubStr("0100110011110011", 5))
# lexilog smallest, size, k times of 1

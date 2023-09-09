class Solution():
    def getLongestPalindrome(self, s:str ) -> str:
        maxLen = 2
        size = len(s)
        res = ""

        for i in range(size):
            l, r = i, i
            while l >= 0 and r <= size -1 and s[l] == s[r]:
                if r -l + 1 > maxLen:
                    maxLen = r -l + 1
                    res = s[l: r + 1]
                elif r -l + 1 == maxLen:
                    res = min(s[l: r + 1], res)
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r <= size -1 and s[l] == s[r]:
                if r -l + 1 > maxLen:
                    maxLen = r -l + 1
                    res = s[l: r + 1]
                elif r -l + 1 == maxLen:
                    res = min(s[l: r + 1], res)
                l -= 1
                r += 1
        return "None" if res == "" else res

so = Solution()
inStr = "YAAAAAGGGXYZABCCBAK"
inStr = "YBBBBBBBGGGXYZABCCBAK"
print(so.getLongestPalindrome(inStr))
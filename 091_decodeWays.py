from functools import lru_cache


class Solution: #L
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res
        val = dfs(0)
        return val

    def numDecodings2(self, s: str) -> int:
        dp = {len(s): 1}
        for i in reversed(range(len(s))):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i < len(s) -1 and ( s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456") ):
                dp[i] += dp[i+2]
        return dp[0]
###############################################
    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)
###########
class Solution:
    def numDecodings(self, s: str) -> int:
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
    #############
    class Solution:
        def numDecodings(self, s: str) -> int:
            if s[0] == "0":
                return 0

            two_back = 1
            one_back = 1
            for i in range(1, len(s)):
                current = 0
                if s[i] != "0":
                    current = one_back
                two_digit = int(s[i - 1: i + 1])
                if two_digit >= 10 and two_digit <= 26:
                    current += two_back
                two_back = one_back
                one_back = current

            return one_back

s = "10"
sol = Solution()
print(sol.numDecodings(s))
print(sol.numDecodings2(s))

"""
91. Decode Ways
Medium

7987

4010

Add to List

Share
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
Accepted
870,407
Submissions
2,781,612
"""
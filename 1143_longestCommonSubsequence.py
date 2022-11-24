from functools import lru_cache
from collections import defaultdict
class Solution: #L
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for x in range(len(text2) + 1)] for y in range(len(text1) + 1)]
#        dp = [[0]*(len(text2) + 1)]*(len(text1) + 1)   This line is not correct, as it will update multiple rows always
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        dp = defaultdict(int)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[(i,j)] = 1 + dp[(i + 1,j + 1)]
                else:
                    dp[(i,j)] = max(dp[(i,j + 1)], dp[(i + 1,j)])

        return dp[(0,0)]

    def longestCommonSubsequenceO(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Option 1: We don't include text1[p1] in the solution.
            option_1 = memo_solve(p1 + 1, p2)

            # Option 2: We include text1[p1] in the solution, as long as
            # a match for it in text2 at or after p2 exists.
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)

            # Return the best option.
            return max(option_1, option_2)

        return memo_solve(0, 0)

    def longestCommonSubsequenceO2(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Recursive case 1.
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            # Recursive case 2.
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        return memo_solve(0, 0)

    def longestCommonSubsequenceO3(self, text1: str, text2: str) -> int:

        # Make a grid of 0's with len(text2) + 1 columns
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]


    def longestCommonSubsequenceO4(self, text1: str, text2: str) -> int:

        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        # The previous and current column starts with all 0's and like
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous

        # The original problem's answer is in previous[0]. Return it.
        return previous[0]

sol = Solution()

text1 = "abcba"
text2 = "abcbcba"
print(sol.longestCommonSubsequence(text1, text2))

text1 = "abcde"
text2 = "ace"
sol = Solution()
print(sol.longestCommonSubsequence(text1, text2))



"""
    1143. Longest Common Subsequence
Medium

8347

96

Add to List

Share
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
 deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters."""
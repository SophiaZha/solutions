class Solution:  # L
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = 0, 0
            while i - l >= 0 and i + r < len(s) and s[i - l] == s[i + r]:
                resLen = r + l + 1
                if resLen >= len(res):
                    res = s[i - l:i + r + 1]
                l += 1
                r += 1

            l, r = 0, 0
            if i + 1 < len(s) and s[i] == s[i + 1]:
                while i - l >= 0 and i + 1 + r < len(s) and s[i - l] == s[i + 1 + r]:
                    resLen = r + l + 2
                    if resLen >= len(res):
                        res = s[i - l: i + r + 2]
                    l += 1
                    r += 1

        return res


"""
5. Longest Palindromic Substring
Medium

21643

1239

Add to List

Share
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
Accepted
2.1M
Submissions
6.5M"""

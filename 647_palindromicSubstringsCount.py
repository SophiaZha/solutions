class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l, r = 0, 0
            while i - l >= 0 and i + r < len(s) and s[i - l] == s[i + r]:
                count += 1
                l += 1
                r += 1

            l, r = 0, 0
            if i + 1 < len(s) and s[i] == s[i + 1]:
                while i - l >= 0 and i + 1 + r < len(s) and s[i - l] == s[i + 1 + r]:
                    count += 1
                    l += 1
                    r += 1

        return count
"""
647. Palindromic Substrings
Medium

8064

176

Add to List

Share
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
Accepted
505,918
Submissions
764,208"""
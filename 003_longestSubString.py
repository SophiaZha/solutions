from builtins import str

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        length = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            length = max(length, i - l + 1)
            charSet.add(s[i])
        return length

str = "pwwkew"
str2 = "abcabcbb"
str3 = "bbbbb"
so = Solution()
print(so.lengthOfLongestSubstring(str))
print(so.lengthOfLongestSubstring(str2))
print(so.lengthOfLongestSubstring(str2))
"""
3. Longest Substring Without Repeating Characters
Medium
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
3,738,927
Submissions
11,115,505
"""
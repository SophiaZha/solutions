from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

    def letterCombinationsL(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        q = deque(d[int(digits[0])])

        for i in range(1, len(digits)):
            s = len(q)
            while s:
                out = q.popleft()
                for j in d[int(digits[i])]:
                    q.append(out + j)
                s -= 1
        return q

    def letterCombinations9(self, digits: str) -> List[str]:
        d2c = {
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        q = []
        p = 0
        print(digits[0])
        for c in d2c[digits[0]]:
            q.append(c)
        while q:
            p += 1
            if p == len(digits):
                return q

            for i in range(len(q)):
                st = q.pop(0)
                if len(st) < len(digits):
                    for c in d2c[digits[p]]:
                        q.append(st + c)
sol = Solution()
digits = "23"
print(sol.letterCombinations9(digits))
digits = ""
print(sol.letterCombinationsL(digits))
print(sol.letterCombinations9(digits))
digits = "2"
print(sol.letterCombinations9(digits))
# print(sol.letterCombinations(digits))
# print(sol.letterCombinationsL(digits))




"""
17. Letter Combinations of a Phone Number
Medium

12489

753

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
Accepted
1,352,665
Submissions
2,447,725
"""
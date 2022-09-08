from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def recursive(openN, closeN):
            if openN == closeN == n:
                return res.append("".join(stack))

            if openN < n:
                stack.append("(")
                recursive(openN + 1, closeN)
                stack.pop()

            if openN > closeN:
                stack.append(")")
                recursive(openN, closeN + 1)
                stack.pop()

        recursive(0, 0)
        return res



so = Solution()
print(so.generateParenthesis(3))


"""
22. Generate Parentheses
Medium

14802

558

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
Accepted
1,181,531
Submissions
1,656,209
"""
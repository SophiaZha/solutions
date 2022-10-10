class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign
"""
371. Sum of Two Integers
Medium

3050

4351

Add to List

Share
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
Accepted
339,517
Submissions
670,149
"""
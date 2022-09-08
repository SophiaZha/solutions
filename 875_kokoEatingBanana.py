from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2
            this_hour = 0

            for p in piles:
                this_hour += (p - 1) // m + 1

            if this_hour > h:
                l = m + 1
            else:
                this_hour <= h
                k = m
                r = m - 1

        return k


piles = [312884470]
h = 312884469
so = Solution()
print(so.minEatingSpeed(piles, h))

"""
875. Koko Eating Bananas
Medium

4943

221

Add to List

Share
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
Accepted
218,265
Submissions
411,701
"""
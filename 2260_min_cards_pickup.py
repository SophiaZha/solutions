from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("inf")
        hash = defaultdict(int)
        for i in range(len(cards)):
            if hash[cards[i]]:
                res = min(res, i - hash[cards[i]] + 2)
            hash[cards[i]] = i + 1
        return res if res != float("inf") else -1

"""
2260. Minimum Consecutive Cards to Pick Up
Medium

You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among
 the picked cards. If it is impossible to have matching cards, return -1.

 

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

 

Constraints:

    1 <= cards.length <= 105
    0 <= cards[i] <= 106

Accepted
32,564
Submissions
62,820
Seen this question in a real interview before?
Longest Substring Without Repeating Characters
Medium
Iterate through the cards and store the location of the last occurrence of each number.
What data structure could you use to get the last occurrenc
"""
from typing import List
class Solution:
    def combineNN(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(start, comb):
            print(" in i = ", start , " comb = ", comb)
            if len(comb) == k:
                print(comb)
                res.append(comb.copy())
                return
            for i in range(start, n+1):
                print(" range i = ", i, end="")
                comb.append(i)
                helper(i+1, comb)
                print(" pop ", comb.pop(), end="")
        helper(1, [])
        return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        sub, res = [], []
        def dfs(i, sub):
            if i > n + 1:
                return
            if i <= n + 1 and len(sub) == k:
                res.append(sub[:])
                return
            sub.append(i)
            dfs(i + 1, sub)
            sub.pop()
            dfs(i + 1, sub)
        dfs(1, sub)
        return res

n = 4
k = 3
so = Solution()
print(so.combine(n, k))
print(so.combineNN(n, k))

"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
Accepted
804.7K
Submissions
1.2M
Acceptance Rate
69.4%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (54)
"""
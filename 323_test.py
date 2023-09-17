from collections import Counter
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [k for k in range(n)]
        rank = [1] * n

        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
            return p

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                par[py] = px
                rank[px] += rank[py]
            else:
                par[px] = py
                rank[py] += rank[px]
            return

        for x, y in edges:
            union(x, y)
        return len(Counter(par))

so = Solution()
n = 4
edges = [[0,1],[2,3],[1,2]]
print(so.countComponents(n, edges))
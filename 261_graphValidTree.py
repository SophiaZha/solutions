# Problem is free on Lintcode  https://www.lintcode.com/problem/178/description
from collections import deque
from typing import List


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
#############################  L Easier to understand, remove parent route
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()

        def dfs(x):
            if x in visited:
                return False
            visited.add(x)

            for nei in adj[x]:
                adj[nei].remove(x)
                if not dfs(nei):
                    return False
            return True

        return dfs(0) and len(visited) == n
########################################### Iterative DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()
        stack = deque([0])

        while stack:
            x = stack.popleft()
            if x in visited:
                return False
            visited.add(x)

            for nei in adj[x]:
                adj[nei].remove(x)
                stack.append(nei)

        return len(visited) == n


"""
261. Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

Difficulty:
"""
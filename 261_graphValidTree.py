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
####################### iterative DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        count = 0
        for s in range(n):
            if s not in visited:
                count += 1
                stack = deque([s])
                while stack:
                    x = stack.popleft()
                    if x in visited:
                        continue
                    visited.add(x)
                    for nei in adj[x]:
                        if x in adj[nei]:
                            adj[nei].remove(x)
                        stack.append(nei)

        return count
##################################################################### O
class UnionFind:

    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        # We use this to keep track of the size of each set.
        self.size = [1] * n

    # The find method, with path compression. There are ways of implementing
    # this elegantly with recursion, but the iterative version is easier for
    # most people to understand!
    def find(self, A):
        # Step 1: Find the root.
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        # Step 2: Do a second traversal, this time setting each node to point
        # directly at A as we go.
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root

    # The union method, with optimization union by size. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # We want to ensure the larger set remains the root.
        if self.size[root_A] < self.size[root_B]:
            # Make root_B the overall root.
            self.parent[root_A] = root_B
            # The size of the set rooted at B is the sum of the 2.
            self.size[root_B] += self.size[root_A]
        else:
            # Make root_A the overall root.
            self.parent[root_B] = root_A
            # The size of the set rooted at A is the sum of the 2.
            self.size[root_A] += self.size[root_B]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False

        # Create a new UnionFind object with n nodes.
        unionFind = UnionFind(n)

        # Add each edge. Check if a merge happened, because if it
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False

        # If we got this far, there's no cycles!
        return True

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
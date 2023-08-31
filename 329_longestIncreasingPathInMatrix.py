from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j, pre_val):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or matrix[i][j] <= pre_val:
                return 0
            if ( i, j) in dp:
                return dp[(i, j)]
            path = 1
            path = max(path, 1 + dfs(i + 1, j, matrix[i][j]))
            path = max(path, 1 + dfs(i, j + 1, matrix[i][j]))
            path = max(path, 1 + dfs(i -1,  j, matrix[i][j]))
            path = max(path, 1 + dfs(i, j - 1, matrix[i][j]))
            dp[(i, j)] = path
            return path

        for i in range(ROWS):
            for j in range(COLS):
                dfs( i, j , -1)
        return max(dp.values())

 """
329. Longest Increasing Path in a Matrix
Hard
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
Accepted
403,704
Submissions
776,496
"""

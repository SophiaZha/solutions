from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])

        def dfs(r, c):
            if (r not in range(row)
                    or c not in range(col)
                    or board[r][c] == "E"
                    or board[r][c] == "X"
            ):
                return
            else:
                board[r][c] = "E"

            for (x, y) in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (x in range(1, row - 1) and y in range(1, col - 1) and board[x][y] == "O"):
                    dfs(x, y)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for i in range(col):
            dfs(0, i)
            dfs(row - 1, i)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "E":
                    board[r][c] = "O"

        return board
################################################L BFS
from itertools import product


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        boards = list(product(range(rows), [0, cols - 1])) + list(product([0, rows - 1], range(cols)))
        print(boards)

        def bfs(m, n):
            q = deque([(m, n)])
            while q:
                r, c = q.popleft()   # change to pop() to make it DFS instead of BFS
                if board[r][c] != "O":
                    continue
                board[r][c] = "E"
                for (x, y) in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (x in range(rows) and y in range(cols) and board[x][y] == "O"):
                        q.append((x, y))

        for r, c in boards:
            if board[r][c] == "O":
                bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
"""
130. Surrounded Regions
Medium

5742

1346

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
Accepted
464,772
Submissions
1,308,034
"""
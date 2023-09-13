import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

#############################L  Time O(N*M); Space O(N*M)

    def orangesRotting2(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            time += 1
            for i in range(len(q)):
                (r, c) = q.popleft()
                for (x, y) in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                    if (x in range(rows) and
                            y in range(cols) and
                            grid[x][y] == 1
                    ):
                        q.append((x, y))
                        grid[x][y] = 2
                        fresh -= 1

        return time if fresh == 0 else -1

################################ O in place, Time O(n^2 * M^2); Space O(1)
    def orangesRotting3(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # run the rotting process, by marking the rotten oranges with the timestamp
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def runRottingProcess(timestamp):
            # flag to indicate if the rotting process should be continued
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # current contaminated cell
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # this fresh orange would be contaminated next
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued

        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1
        # end of process, to check if there are still fresh oranges left
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1
        # return elapsed minutes if no fresh orange left
        return timestamp - 2

    def orangesRottingL(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, q = 0, []
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.pop(0)
                for x, y in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                    if ( x in range(rows) and y in range(cols) and grid[x][y] ==1
                    ):
                        grid[x][y] = 2
                        q.append((x, y))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

so = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(so.orangesRottingL(grid))

"""
994. Rotting Oranges
Medium

8307

304

Add to List

Share
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
Accepted
481,691
Submissions
920,611
"""
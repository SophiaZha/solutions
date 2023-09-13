from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

############
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]:
            return []

        num_rows, num_cols = len(matrix), len(matrix[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))

        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Check all 4 directions
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return reachable

        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))

#######################################################L
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pq = deque()
        aq = deque()
        rows, cols = len(heights), len(heights[0])

        for i in range(rows):
            pq.append((i, 0))
            aq.append((i, cols - 1))

        for i in range(cols):
            pq.append((0, i))
            aq.append((rows - 1, i))

        def bfs(queue):
            reachable = set()
            while queue:
                r, c = queue.pop()
                reachable.add((r, c))

                for (x, y) in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (x not in range(rows)
                            or y not in range(cols)
                            or (x, y) in reachable
                    ):
                        continue
                    if heights[x][y] < heights[r][c]:
                        continue
                    queue.append((x, y))
            return reachable

        a_reachable = bfs(aq)
        p_reachable = bfs(pq)

        return list(a_reachable.intersection(p_reachable))

###########################################################L
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, reachable):

            reachable.add((r, c))

            for (x, y) in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                if (x not in range(rows)
                        or y not in range(cols)
                        or (x, y) in reachable
                ):
                    continue

                if heights[x][y] < heights[r][c]:
                    continue

                dfs(x, y, reachable)

        p_reachable = set()
        a_reachable = set()
        # for i in range(rows):
        #     for j in range(cols):
        #         if i == 0 or j == 0:
        #             dfs(i, j, pset)
        #         if i == rows - 1 or j == cols - 1:
        #             dfs(i, j, aset)
        for i in range(rows):
            dfs(i, 0, p_reachable)
            dfs(i, cols - 1, a_reachable)

        for i in range(cols):
            dfs(0, i, p_reachable)
            dfs(rows - 1, i, a_reachable)

        return list(a_reachable.intersection(p_reachable))

"""
417. Pacific Atlantic Water Flow
Medium

5575

1049

Add to List

Share
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
Accepted
295,737
Submissions
551,560
"""
import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col, row, box = collections.defaultdict(set),collections.defaultdict(set),collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if( board[i][j] == "."):
                    continue
                if (board[i][j] in row[i] or
                   board[i][j] in col[j] or
                   board[i][j] in box[(i//3, j//3)]):
                   return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i//3, j//3)].add(board[i][j])
        return True

    def isValidSudokuL(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in boxes[ ((r//3)*3 + c//3)] ) :
                   return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[((r//3)*3 + c//3)].add(board[r][c])
        return True

    def isValidSudokuL2(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) -1
                if rows[r][pos] == 1:
                    return False
                else:
                    rows[r][pos] = 1

                if cols[c][pos] == 1:
                    return False
                else:
                    cols[c][pos] = 1

                if boxes[ (r//3)* 3 + c//3 ][pos] == 1:
                    return False
                else:
                    boxes[ (r//3)* 3 + c//3 ][pos] = 1
        return True

so = Solution()

board =\
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(so.isValidSudoku(board))
board =\
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(so.isValidSudoku(board))

"""
36. Valid Sudoku
Medium

6188

787

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
Accepted
847,383
Submissions
1,504,675
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b, mid = 0, len(matrix) - 1, 0
        while t <= b:
            mid = (t + b) // 2
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                break
        if not t <= b:
            return False

        row = (t + b) // 2

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True

        return False


"""
74. Search a 2D Matrix
Medium

9386

300

Add to List

Share
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
Accepted
952,077
Submissions
2,059,315

"""
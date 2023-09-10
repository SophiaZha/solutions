from typing import List
class Solution:
    def getHopSkip(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        visited = [[False] * c for _ in range(r)]
        currR, currC = 0, 0
        dxdy = ((1, 0), (0, 1), (-1, 0), (0, -1))
        index = 0
        visited[currR][currC] = True
        while True:
            for i in range(2):
                nextR, nextC = currR + dxdy[index][0], currC + dxdy[index][1]
                tempR, tempC = currR, currC
                if nextR == r or nextC == c or nextR == -1 or nextC == -1 or visited[nextR][nextC]:
                    index += 1
                    index %= 4
                    currR += dxdy[index][0]
                    currC += dxdy[index][1]
                else:
                    currR, currC = nextR, nextC
                if visited[currR][currC]:
                    if i == 0:
                        return matrix[tempR][tempC]
                    else:
                        return matrix[tempR - dxdy[index - 1][0]][tempC - dxdy[index - 1][1]]
                visited[currR][currC] = True
        return 0


so = Solution()
# r, c = map(int, input().split())
# matrix = []
# for i in range(r):
#     matrix.append([int(j) for j in input().split()])
matrix1 = [
    [29, 8, 1],
    [15, 41, 2],
    [25, 51, 4],
    [65, 61, 3],
    [75, 71, 73]
]
# matrix1 = [
#     [29, 8, 37, 0, 5],
#     [15, 42, 3, 9, 2],
#     [1, 10, 14, 12, 40],
#     [59, 58, 57, 50, 55],
#     [61, 62, 63, 64, 65],
# ]
print(so.getHopSkip(matrix1))
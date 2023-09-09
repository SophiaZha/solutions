from typing import List
class Solution:  # half cooked
    def getHopSkip(self, matrix: List[List[int]])-> int:
        rows, cols = len(matrix), len(matrix[0])
        visited = []
        skipped = []
        directions = [ [0, 1], [1, 0], [0, -1], [-1, 0] ]
        nextDirect = 0
        start = [0,0]
        visited.append(start)
        while True:
            tmpPoint = start + directions[nextDirect]
            adjustDirect = (nextDirect + 1) % 4
            if tmpPoint not in visited and tmpPoint[0] in range(rows) and tmpPoint[1] in range(cols):
                skipped.append(tmpPoint)
            else:
                tmpPoint = start + directions[ ]
            nextDirect =     (nextDirect + 1 ) % 4

            if tmpPoint not in visited and tmpPoint[0] in range(rows) and tmpPoint[1] in range(cols):
                visited.append(tmpPoint)
            else:
                tmpPoint = start + directions[ (nextDirect + 1 ) % 4]











        return 0



matrix = [
    [29, 8, 37],
    [15, 41, 3],
    [1, 10, 14]
]







class Solution:
    def isWordInMatrix(self):
        rows, cols = map(int, input().split())
        # rows, cols = int(rows), int(cols)
        strPool = set()
        matrix = []
        res = ""
        for i in range(rows):
            matrix.append([j for j in input().split()])
        for i in range(rows):
            rowstr = ""
            for j in range(cols):
                rowstr += matrix[i][j]
                strPool.add(rowstr)
                strPool.add(reversed(rowstr))

        for i in range(cols):
            colstr = ""
            for j in range(rows):
                colstr += matrix[j][i]
                strPool.add(colstr)
                strPool.add(reversed(colstr))

        counts = int(input())
        words = [s for s in input().split()]
        for i in range(counts):
            if words[i] in strPool:
                res += "Yes "
            else:
                res += "No "
        return res[0:-1]


so = Solution()
print(so.isWordInMatrix())
# 3 3
# C A T
# I D O
# N O M
# 4
# CAT TOM ADO MOM
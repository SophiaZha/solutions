class intCounts:
    def getSum(self, n: int) -> int:
        if n == 1:
            return "1"
        st = "1"
        for i in range(1, n):
            st = self.getNextStr(st)
        return sum(int(s) for s in st )

    def getNextStr(self, instr:str) ->str:
        ct, st , res = 0, "", ""
        n = len(instr)
        if n == 1:
            return "1" + instr[0]
        for i, s in enumerate(instr):
            if i == 0:
                ct = 1
                st = s
            else:
                if s == st:
                    ct += 1
                else:
                    res += str(ct) + st
                    ct, st = 1, s
            if i == n -1:
                res += str(ct) + s
        return res
so = intCounts()
print(so.getNextStr("1"))
print(so.getNextStr("11"))
print(so.getNextStr("21"))
print(so.getNextStr("1211"))
print(so.getNextStr("111221"))
print(so.getNextStr("312211"))
print(so.getNextStr("13112221"))
print(so.getSum(2))
print(so.getSum(3))
print(so.getSum(4))
print(so.getSum(5))
print(so.getSum(6))

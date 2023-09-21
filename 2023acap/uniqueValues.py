from typing import List
class Solution:
    def getUniqueValues(self, alist:List[int], blist: List[int], k:int)->int:
        aset = set(alist)
        bset = set(blist)
        uset = aset.union(bset)
        res =  min( min( (len(uset) - len(aset)), k ) + len(aset), len(alist) )
        return res

a = [2,2,2,2,2]
b = [1,4,6,8,1]
so = Solution()
print(so.getUniqueValues(a, b, 2))
print(so.getUniqueValues(a, b, 9))
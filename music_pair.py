from collections import defaultdict
from typing import List

class Solution:
    def music(selfself, arr:List[int], n: int) ->int:
        hash = defaultdict(int)
        res = 0
        for num in arr:
            if hash[(60-num % 60)% 60] > 0:
                hash[ 60- max % 60) % 60] -= 1
                res += 1
            else:
                hash[num % 60] += 1
        return res


arr = [3, 60, 60, 60]
so = Solution()
print(so.music(arr, 4))

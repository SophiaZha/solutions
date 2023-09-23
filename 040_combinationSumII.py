from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(cur, pos, target):
            print('calling backtrack cur = ', cur, ", pos = ", pos, ", target = " , target , end=" ")
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                print("candidates[", i, "] = ", candidates[i], " prev = ", prev, end=" ")
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                print("appending candidates[", i, "] = ", candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                print("pop cur [", (len(cur) -1), "] = ", cur[-1])
                cur.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res
candidates = [10,1,2,7,6,1,5]  # 1, 1, 2, 5, 6, 7, 10,
target = 8
so = Solution()
print(so.combinationSum2(candidates, target))


"""
40. Combination Sum II
Medium

6818

167

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
Accepted
639,484
Submissions
1,203,538
"""

"""
C:\Users\user\AppData\Local\Microsoft\WindowsApps\python3.9.exe C:/Users/user/PycharmProjects/solutions/040_combinationSumII.py 
calling backtrack cur =  [] , pos =  0 , target =  8 candidates[ 0 ] =  1  prev =  -1 appending candidates[ 0 ] =  1
calling backtrack cur =  [1] , pos =  1 , target =  7 candidates[ 1 ] =  1  prev =  -1 appending candidates[ 1 ] =  1
calling backtrack cur =  [1, 1] , pos =  2 , target =  6 candidates[ 2 ] =  2  prev =  -1 appending candidates[ 2 ] =  2
calling backtrack cur =  [1, 1, 2] , pos =  3 , target =  4 candidates[ 3 ] =  5  prev =  -1 appending candidates[ 3 ] =  5
calling backtrack cur =  [1, 1, 2, 5] , pos =  4 , target =  -1 pop cur [ 3 ] =  5
candidates[ 4 ] =  6  prev =  5 appending candidates[ 4 ] =  6
calling backtrack cur =  [1, 1, 2, 6] , pos =  5 , target =  -2 pop cur [ 3 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [1, 1, 2, 7] , pos =  6 , target =  -3 pop cur [ 3 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [1, 1, 2, 10] , pos =  7 , target =  -6 pop cur [ 3 ] =  10
pop cur [ 2 ] =  2
candidates[ 3 ] =  5  prev =  2 appending candidates[ 3 ] =  5
calling backtrack cur =  [1, 1, 5] , pos =  4 , target =  1 candidates[ 4 ] =  6  prev =  -1 appending candidates[ 4 ] =  6
calling backtrack cur =  [1, 1, 5, 6] , pos =  5 , target =  -5 pop cur [ 3 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [1, 1, 5, 7] , pos =  6 , target =  -6 pop cur [ 3 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [1, 1, 5, 10] , pos =  7 , target =  -9 pop cur [ 3 ] =  10
pop cur [ 2 ] =  5
candidates[ 4 ] =  6  prev =  5 appending candidates[ 4 ] =  6
calling backtrack cur =  [1, 1, 6] , pos =  5 , target =  0 pop cur [ 2 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [1, 1, 7] , pos =  6 , target =  -1 pop cur [ 2 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [1, 1, 10] , pos =  7 , target =  -4 pop cur [ 2 ] =  10
pop cur [ 1 ] =  1
candidates[ 2 ] =  2  prev =  1 appending candidates[ 2 ] =  2
calling backtrack cur =  [1, 2] , pos =  3 , target =  5 candidates[ 3 ] =  5  prev =  -1 appending candidates[ 3 ] =  5
calling backtrack cur =  [1, 2, 5] , pos =  4 , target =  0 pop cur [ 2 ] =  5
candidates[ 4 ] =  6  prev =  5 appending candidates[ 4 ] =  6
calling backtrack cur =  [1, 2, 6] , pos =  5 , target =  -1 pop cur [ 2 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [1, 2, 7] , pos =  6 , target =  -2 pop cur [ 2 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [1, 2, 10] , pos =  7 , target =  -5 pop cur [ 2 ] =  10
pop cur [ 1 ] =  2
candidates[ 3 ] =  5  prev =  2 appending candidates[ 3 ] =  5
calling backtrack cur =  [1, 5] , pos =  4 , target =  2 candidates[ 4 ] =  6  prev =  -1 appending candidates[ 4 ] =  6
calling backtrack cur =  [1, 5, 6] , pos =  5 , target =  -4 pop cur [ 2 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [1, 5, 7] , pos =  6 , target =  -5 pop cur [ 2 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [1, 5, 10] , pos =  7 , target =  -8 pop cur [ 2 ] =  10
pop cur [ 1 ] =  5
candidates[ 4 ] =  6  prev =  5 appending candidates[ 4 ] =  6
calling backtrack cur =  [1, 6] , pos =  5 , target =  1 candidates[ 5 ] =  7  prev =  -1 appending candidates[ 5 ] =  7
calling backtrack cur =  [1, 6, 7] , pos =  6 , target =  -6 pop cur [ 2 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [1, 6, 10] , pos =  7 , target =  -9 pop cur [ 2 ] =  10
pop cur [ 1 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [1, 7] , pos =  6 , target =  0 pop cur [ 1 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [1, 10] , pos =  7 , target =  -3 pop cur [ 1 ] =  10
pop cur [ 0 ] =  1
candidates[ 1 ] =  1  prev =  1 candidates[ 2 ] =  2  prev =  1 appending candidates[ 2 ] =  2
calling backtrack cur =  [2] , pos =  3 , target =  6 candidates[ 3 ] =  5  prev =  -1 appending candidates[ 3 ] =  5
calling backtrack cur =  [2, 5] , pos =  4 , target =  1 candidates[ 4 ] =  6  prev =  -1 appending candidates[ 4 ] =  6
calling backtrack cur =  [2, 5, 6] , pos =  5 , target =  -5 pop cur [ 2 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [2, 5, 7] , pos =  6 , target =  -6 pop cur [ 2 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [2, 5, 10] , pos =  7 , target =  -9 pop cur [ 2 ] =  10
pop cur [ 1 ] =  5
candidates[ 4 ] =  6  prev =  5 appending candidates[ 4 ] =  6
calling backtrack cur =  [2, 6] , pos =  5 , target =  0 pop cur [ 1 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [2, 7] , pos =  6 , target =  -1 pop cur [ 1 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [2, 10] , pos =  7 , target =  -4 pop cur [ 1 ] =  10
pop cur [ 0 ] =  2
candidates[ 3 ] =  5  prev =  2 appending candidates[ 3 ] =  5
calling backtrack cur =  [5] , pos =  4 , target =  3 candidates[ 4 ] =  6  prev =  -1 appending candidates[ 4 ] =  6
calling backtrack cur =  [5, 6] , pos =  5 , target =  -3 pop cur [ 1 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [5, 7] , pos =  6 , target =  -4 pop cur [ 1 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [5, 10] , pos =  7 , target =  -7 pop cur [ 1 ] =  10
pop cur [ 0 ] =  5
candidates[ 4 ] =  6  prev =  5 appending candidates[ 4 ] =  6
calling backtrack cur =  [6] , pos =  5 , target =  2 candidates[ 5 ] =  7  prev =  -1 appending candidates[ 5 ] =  7
calling backtrack cur =  [6, 7] , pos =  6 , target =  -5 pop cur [ 1 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [6, 10] , pos =  7 , target =  -8 pop cur [ 1 ] =  10
pop cur [ 0 ] =  6
candidates[ 5 ] =  7  prev =  6 appending candidates[ 5 ] =  7
calling backtrack cur =  [7] , pos =  6 , target =  1 candidates[ 6 ] =  10  prev =  -1 appending candidates[ 6 ] =  10
calling backtrack cur =  [7, 10] , pos =  7 , target =  -9 pop cur [ 1 ] =  10
pop cur [ 0 ] =  7
candidates[ 6 ] =  10  prev =  7 appending candidates[ 6 ] =  10
calling backtrack cur =  [10] , pos =  7 , target =  -2 pop cur [ 0 ] =  10
[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

Process finished with exit code 0
"""
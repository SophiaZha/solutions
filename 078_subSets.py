from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp_res = []
        def dfs(i):
            print("dfs(", i, ") ")
            if (i == len(nums)):
                res.append(tmp_res.copy())
                print(" res for = " + str(res) )
                return
            else:
                print("t0 for ", i, " = " + str(res), end="___")
                tmp_res.append(nums[i])
                print("t1 for ", i, " = " + str(tmp_res), end="___")
                dfs(i + 1)
                tmp_res.pop()
                print("t2 for ", i, " = " + str(tmp_res), end="...")
                dfs(i + 1)
        dfs(0)
        return res

    def subset2(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        if not nums:
            return subsets
        for num in nums:
            for idx in range(len(subsets)):
                subsets.append(subsets[idx]+[num])
        return subsets

    def subset3(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        if not nums:
            return subsets
        for num in nums:
            for idx in range(len(subsets)):
                subsets = subsets + [subsets[idx]+[num]]
        return subsets

    def subsets4(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

    def subsetsB(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            print("bitmask for ", n, " is ", bitmask)

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output

    def subsetsB2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        nth_bit = 1 << n
        for i in range(2 ** n):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i | nth_bit)[3:]
            print("bitmask for ", n, " is ", bitmask)

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output

    def subsets0(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        for i in range(2**N, 2**(N+1)):
            bitmap = bin(i)[3:]
            tmp = [ nums[k] for k in range(N) if bitmap[k] == '1']
            print(bin(i) + ", "+bin(i)[3:] + ", " + str(tmp))
            res.append(tmp)
        return res

mynum = [1, 2, 3]
x = Solution()
print(x.subsets(mynum))
# print(x.subset2(mynum))
# print(x.subset3(mynum))
# print(x.subsets4(mynum))
# print(x.subsetsB(mynum))
# print(x.subsetsB2(mynum))

""" 
78. Subsets
Medium
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
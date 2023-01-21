# Find the indexes of max values in a given array - not sure return only one or multiples, let us prepare for multiples
# If there are multiple max values, return either one with equal probability
#the array may o rmay not contain multiple copies of maximum number]such that each index
# (which contains the maximum numbers)have the probability of 1/no of maxnumbers to be returned
# [-1, 3, 2, 3, 3 ] have the probablities of 1/3 to return 1, 3 or 4
import random
from typing import List

class Solution:
    def indexOfMax(self, nums : List[int]) -> int:
        max = 0
        index = -1
        for i,value in enumerate(nums):
            if value> max:
                max = value
                index = i
        return index

    def getOneIndexOfMax(self, nums:List[int]) -> int:
        count = 0
        maxNum = nums[0]
        indexList = []
        for i, value in enumerate(nums):
            if value == maxNum:
                indexList.append(i)
            elif value > maxNum:
                indexList.clear()
                indexList.append(i)
                maxNum = value
        return indexList[random.randint(0, len(indexList) -1 )]

so = Solution()
nums = [2,4,8,5,2,1]
print(so.indexOfMax(nums))
nums = [-1, 3, 2, 3, 3 ]
for i in range(100):
    print(so.getOneIndexOfMax(nums), end=" ")
print()
nums = [2,4,6,6,3,1,6,6]
for i in range(100):
    print(so.getOneIndexOfMax(nums), end=" ")





# Given an array of integers, calculate the minimum number of moves to back required to sort the array in ascending order
# moves to back i.e. remove an integer from its initial position and add it back to the end of the array
# size of array > 1
# all values are unique
# https://ledarryl.medium.com/find-the-minimum-number-of-move-backs-required-to-sort-an-array-7bb2bb47ebf6
from typing import List
class Solution:
    def countMoveToBack(self, input:List[int]):
        sorted_arr = sorted(input)
        sorted_index = 0
        for i in range(len(input)):
            if input[i] == sorted_arr[sorted_index]:
                sorted_index += 1
        min_moves = len(input) - sorted_index
        return min_moves
so = Solution()
input = [1,4,2,5,3]
print(so.countMoveToBack(input))


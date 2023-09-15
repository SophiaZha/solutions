from typing import List
class mathQuiz:
    def custom_sort_key(self, num:int ) -> int:
        # Count the number of 1s in the binary representation of the number
        # https://learnpython.com/blog/python-custom-sort-function/
        num_ones = bin(num).count('1')
        return (num_ones, num)  # Sort first by num_ones, then by the original value

    def getSortedArray(self, nums:List[int]) -> List[int]:
        sorted_list = sorted(nums, key=self.custom_sort_key)
        return sorted_list

    def getSortedArrayL(self, nums:List[int]) -> List[int]:
        sorted_list = sorted(nums, key= lambda x: (bin(x).count("1"), x) )
        return sorted_list


so = mathQuiz()
decimal_list = [5, 3, 7, 6, 2, 8]
sorted_result = so.getSortedArray(decimal_list)
print(sorted_result)
sorted_result = so.getSortedArrayL(decimal_list)
print(sorted_result)

so = mathQuiz()
ints = [1,2,3,4]
print(so.getSortedArray(ints))
print(so.getSortedArrayL(ints))

ints = [3, 15, 7, 3,2]
print(so.getSortedArray(ints))
print(so.getSortedArrayL(ints))


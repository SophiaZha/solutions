class Solution:
    def isWordSorted(self, input_string: str) -> int:
        for i in range(1, len(input_string)):
            if input_string[i] < input_string[i - 1]:
                return i
        return 0

so = Solution()

input_str1 = "abcde"
input_str2 = "cabde"
input_str3 = "abdc"

result1 = so.isWordSorted(input_str1)
result2 = so.isWordSorted(input_str2)
result3 = so.isWordSorted(input_str3)

print(f"Result for '{input_str1}': {result1}")
print(f"Result for '{input_str2}': {result2}")
print(f"Result for '{input_str3}': {result3}")

print(so.isWordSorted("abcde"))
print(so.isWordSorted("cabde"))
print(so.isWordSorted("abdc"))

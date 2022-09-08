class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[], [1, 1, 1, 1, 1]]
        a, e, i, o, u = 0, 1, 2, 3, 4
        mod = 10 ** 9 + 7
        for j in range(2, n + 1):
            dp.append([0, 0, 0, 0, 0])
            dp[j][a] = (dp[j - 1][e] + dp[j - 1][i] + dp[j - 1][u]) % mod
            dp[j][e] = (dp[j - 1][a] + dp[j - 1][i]) % mod
            dp[j][i] = (dp[j - 1][e] + dp[j - 1][o]) % mod
            dp[j][o] = (dp[j - 1][i]) % mod
            dp[j][u] = (dp[j - 1][i] + dp[j - 1][o]) % mod
        return sum(dp[n]) % mod

    def countVowelPermutation2(self, n: int) -> int:
        MODULO = 10 ** 9 + 7
        dp = [1] * 5  # number of string end at character i, with i=[a, e, i, o, u]
        for _ in range(1, n):
            a, e, i, o, u = dp
            dp[0] = (e + i + u) % MODULO
            dp[1] = (a + i) % MODULO
            dp[2] = (e + o) % MODULO
            dp[3] = i % MODULO
            dp[4] = (i + o) % MODULO

        return sum(dp) % MODULO

    def count_vowel_permutations(self,n):
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)

so = Solution()
n = 5
print(so.countVowelPermutation(n))
print(so.countVowelPermutation2(n))
print(so.count_vowel_permutations(n))

"""
1220. Count Vowels Permutation
Hard
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
Accepted
96,282
Submissions
158,102
"""

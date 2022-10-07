from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break
        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True
            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True
            visited[char] = False
            res.append(char)
        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

sol = Solution()
words =  [  "wrt",  "wrf",  "er",  "ett",  "rftt"]
print(sol.alienOrder((words)))

words =  [  "wrt",  "wrf",  "er",  "rftt"]
print(sol.alienOrder((words)))

words =  [  "z",  "x",  "z"]
print(sol.alienOrder((words)))


"""
269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
Difficulty:
"""
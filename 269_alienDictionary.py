from collections import defaultdict, deque,  Counter
from typing import List
class Solution:
    def alienOrderL(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        for fw, sw in zip(words, words[1:]):
            for c, d in zip(fw, sw):
                if c != d:
                    adj[c].add(d)
                    break
            else:
                if len(fw) > len(sw):
                    print("length conflicting")
                    return ""
        res = []
        visit = {}
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = False
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visit[c] = True
            print("append res " + c)
            res.append(c)
            return True

        if not all(dfs(c) for c in adj):
            return ""
        res.reverse()
        return "".join(res)

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
###################  O
    def alienOrderD(self, words: List[str]) -> str:
        reverse_adj_list = {c : [] for word in words for c in word}
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    reverse_adj_list[d].append(c)
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True
        if not all(visit(node) for node in reverse_adj_list):
            return ""
        return "".join(output)

    def alienOrderB(self, words: List[str]) -> str:

        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word): return ""

        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)

    def alienOrder7(self, words: List[str]) -> str:
        adj = {i: set() for word in words for i in word}
        in_degree = {i: 0 for word in words for i in word}
        for fw, sw in zip(words, words[1:]):
            for c, d in zip(fw, sw):
                if c != d:
                    if d not in adj[c]:
                        adj[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(fw) > len(sw): return ""

        res = []
        q = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                q.append(c)

        while q:
            c = q.popleft()
            res += c
            for d in adj[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    q.append(d)

        if len(res) < len(in_degree):
            return ""
        return "".join(res)


sol = Solution()
words =  [  "wrt",  "wrf",  "er",  "ett",  "rftt"]
print(sol.alienOrderL((words)))
words =  [  "wrt",  "wrf",  "er",  "rftt"]
#print(sol.alienOrderB((words)))
words =  [  "z",  "x",  "z"]
#print(sol.alienOrderB((words)))
words =  [  "abc",  "ab"]
#print(sol.alienOrderB((words)))



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
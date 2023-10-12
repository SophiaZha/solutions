import collections
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: collections.deque() for src, des in tickets}
        res = ["JFK"]
        tickets.sort()
        for src, des in tickets:
            adj[src].append(des)

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for u in temp:
                res.append(u)
                adj[src].popleft()
                if dfs(u):
                    return res
                adj[src].append(u)
                res.pop()
        dfs("JFK")
        return res

        def findItineraryL(self, tickets: List[List[str]]) -> List[str]:
            res = ["JFK"]
            adj = {s: [] for s, d in tickets}
            tickets.sort()
            for s, d in tickets:
                adj[s].append(d)
            def dfs(s):
                if len(res) == len(tickets) + 1:
                    return True
                if s not in adj:
                    return False

                temp = list(adj[s])
                for i, v in enumerate(temp):
                    adj[s].pop(i)
                    res.append(v)
                    if dfs(v):
                        return True
                    adj[s].insert(i, v)
                    res.pop()
            dfs("JFK")
            return res


    def findItinerary0(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)
        for a, z in tickets:
            adj[a].append(z)
        res = ["JFK"]
        def dfs(a):
            if len(res) == len(tickets) +1:
                return True
            for z in adj[a][:]:
                adj[a].pop(0)
                res.append(z)
                if dfs(z):
                    return res
                res.pop()
                adj[a].append(z)
            return False
        dfs("JFK")
        return res

tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

so = Solution()
print(so.findItinerary(tickets))



"""
    332. Reconstruct Itinerary
Hard

4250

1609

Add to List

Share
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports 
of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
 If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order 
 when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
Accepted
304,914
Submissions
747,739"""
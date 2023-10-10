import collections
from typing import List

class Solution:
    def canFinishL(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = 0
        adj = collections.defaultdict(list)
        req_count = [0]*numCourses
        for crs, req in prerequisites:
            adj[req].append(crs)
            req_count[crs] +=1
        q = []
        for crs in range(numCourses):
            if req_count[crs] == 0:
                q.append(crs)
        while q:
            visited += 1
            allowed_crs = q.pop(0)
            for next_crs in adj[allowed_crs]:
                req_count[next_crs] -=1
                if req_count[next_crs] == 0:
                    q.append(next_crs)
        return visited == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}
        # preMap = [[] for i in range(numCourses)]  ###### this line is equally good as the above one
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
############################################### topological sort
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        req_dict = [[] for i in range(numCourses)]
        for cs, req in prerequisites:
            req_dict[cs].append(req)

        visiting = set()

        def dfs(cs):
            if cs in visiting:
                return False
            if len(req_dict[cs]) == 0:
                return True

            visiting.add(cs)
            for req in req_dict[cs]:
                if not dfs(req):
                    return False
                else:
                    req_dict[cs].remove(req)

            visiting.remove(cs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    def canFinish3(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depList = collections.defaultdict(list)
        visited, cycle = set(), set()

        for crs, dep in prerequisites:
            depList[crs].append(dep)

        def dfs(i):
            if i in visited:
                return True
            elif i in cycle:
                return False
            cycle.add(i)
            for dep in depList[i]:
                if dfs(dep) == False:
                    return False
            cycle.remove(i)
            visited.add(i)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True

    def canFinish9(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for crs, req in prerequisites:
            adj[crs].append(req)
        visiting = set()
        def dfs(crs):
            visiting.add(crs)
            for req in adj[crs][:]:
                if req in visiting:
                    return False
                if dfs(req):
                    adj[crs].remove(req)
                else:
                    return False
            visiting.remove(crs)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
n = 4
pre = [[2,0],[1,0],[3,1],[3,2],[1,3]]
so = Solution()
print(so.canFinish2(n, pre))
print(so.canFinish3(n, pre))
print(so.canFinish(n, pre))
print(so.canFinishL(n, pre))
print(so.canFinish9(n, pre))



"""
207. Course Schedule
Medium

11304

439

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
Accepted
1,007,078
Submissions
2,223,174
"""
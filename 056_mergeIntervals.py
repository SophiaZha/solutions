from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = []
        output.append(intervals[0])
        for start, end in intervals[1:]:
            if output[-1][1] < start:
                output.append([start, end])
            else:
                output[-1][0] = min(output[-1][0], start)
                output[-1][1] = max(output[-1][1], end)
        return output

    def mergeL(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        [a, z] = intervals[0]
        for i in range(1, len(intervals)):
            if z < intervals[i][0]:
                res.append([a,z])
                [a, z] = intervals[i]
            else:
                a, z = min(a, intervals[i][0]), max(z, intervals[i][1])
        res.append([a, z])
        return res

    def mergeLL(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        res.append(intervals[0])
        for na, nz in intervals[1:]:
            if res[-1][1] >= na:
                res[-1][1] = max(res[-1][1], nz)
            else:
                res.append([na, nz])
        return res
"""
56. Merge Intervals
Medium

16390

585

Add to List

Share
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Accepted
1,660,637
Submissions
3,626,067
"""
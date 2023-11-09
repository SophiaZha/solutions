class Solution: #L
    def canAttendMeetings(self, intervals):
        intervals.sort()

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True

    def canAttendMeetingsL(self, intervals):
        if len(intervals) == 0:
            return True
        intervals.sort()
        preEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if preEnd > start:
                return False
            else:
                preEnd = end
        return True


"""
252. Meeting Rooms
Easy

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

 

Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti < endi <= 106

"""
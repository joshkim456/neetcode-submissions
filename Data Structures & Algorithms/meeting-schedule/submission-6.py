"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = []

        for interval in intervals:
            meetings.append([interval.start, interval.end])
        
        meetings.sort()

        i = 0
        while i < len(meetings)-1:
            if meetings[i][1] > meetings[i+1][0]:
                return False
            i += 1
        return True
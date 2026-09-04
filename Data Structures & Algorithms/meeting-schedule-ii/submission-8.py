"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sortedStart = []
        sortedEnd = []

        for interval in intervals:
            sortedStart.append(interval.start)
            sortedEnd.append(interval.end)

        sortedStart.sort()
        sortedEnd.sort()

        count = 0

        i = 0
        j = 0

        ans = 0

        while i < len(sortedStart):
            if sortedStart[i] < sortedEnd[j]: 
                count += 1 
                ans = max(ans, count)
                i += 1
            else: 
                count -= 1
                j += 1
        
        return ans
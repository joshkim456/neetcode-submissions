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

        ans = 0
        count = 0

        l = 0
        r = 0

        while l < len(sortedStart):
            if sortedStart[l] < sortedEnd[r]:
                count += 1
                ans = max(ans, count)
                l += 1
            else:
                count -= 1
                r += 1

        return ans


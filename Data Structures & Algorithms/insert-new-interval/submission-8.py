import heapq

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0] and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        runningMin = newInterval[0]
        runningMax = newInterval[1]

        while i < len(intervals) and intervals[i][0] <= newInterval[1] and intervals[i][1] >= newInterval[0]:
            runningMin = min(runningMin, intervals[i][0], newInterval[0])
            runningMax = max(runningMax, intervals[i][1], newInterval[1])
            i += 1
        output.append([runningMin, runningMax])

        while i < len(intervals) and newInterval[1] < intervals[i][0]:
            output.append(intervals[i])
            i += 1
 
        return output
                

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []

        i = 0
        while i < len(intervals):
            runningMin = intervals[i][0]
            runningMax = intervals[i][1]
            j = i
            while j < len(intervals)-1 and runningMax >= intervals[j+1][0]:
                runningMax = max(runningMax, intervals[j+1][1])
                j += 1
            i = j+1
            output.append([runningMin, runningMax])
        return output
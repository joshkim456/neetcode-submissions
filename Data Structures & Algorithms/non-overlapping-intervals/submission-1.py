class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = float('-inf')
        total = 0

        for i in range(len(intervals)):
            if prevEnd > intervals[i][0]:
                prevEnd = min(prevEnd, intervals[i][1])
                total += 1
            else:
                prevEnd = intervals[i][1]
        
        return total
        

[1, 2], [1, 4], [2, 4]

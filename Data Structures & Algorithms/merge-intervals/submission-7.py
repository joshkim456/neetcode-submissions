class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        intervals.sort()

        i = 0

        while i < len(intervals):
            mini, maxi = intervals[i][0], intervals[i][1]
            j = i
            while j < len(intervals)-1 and maxi >= intervals[j+1][0]:
                maxi = max(maxi, intervals[j+1][1])
                j += 1
            i = j + 1
            output.append([mini, maxi])
        
        return output
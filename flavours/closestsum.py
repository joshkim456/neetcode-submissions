from typing import List

class Solution:
    def closestSum(self, numbers: List[int], target: int) -> int:
        l = 0
        r = len(numbers)-1

        ans = 0
        smallestDiff = float('inf')

        while l < r:
            totalDiff = abs(target - (numbers[l] + numbers[r]))
            
            if totalDiff < smallestDiff:
                smallestDiff = totalDiff
                ans = numbers[l] + numbers[r] 
            elif totalDiff == smallestDiff:
                if ans > numbers[l] + numbers[r]:
                    ans = numbers[l] + numbers[r]

            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return numbers[l] + numbers[r]

        return ans
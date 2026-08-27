from typing import List

class Solution:
    def countPairs(self, numbers: List[int], target: int) -> int:
        
        l = 0
        r = len(numbers)-1

        count = 0

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                if numbers[l] == numbers[r]:
                    m = r - l + 1
                    count += m*(m-1)//2
                    break

                tempL = l
                tempR = r
                leftCount = 0
                rightCount = 0
                while numbers[tempL] == numbers[l]:
                    tempL += 1
                    leftCount += 1
                while numbers[tempR] == numbers[r]:
                    tempR -= 1
                    rightCount += 1
                count += leftCount * rightCount
                l = tempL
                r = tempR

        return count
                

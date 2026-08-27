from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)

        l = 0 
        r = len(nums)-1

        for i in range(len(squares)-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                squares[i] = nums[l]*nums[l]
                l += 1
            else:
                squares[i] = nums[r]*nums[r]
                r -= 1
        
        return squares
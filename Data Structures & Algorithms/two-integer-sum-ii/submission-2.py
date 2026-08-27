class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            req = target - n
            if req in seen:
                return [seen[req], i+1]
            
            seen[n] = i+1 
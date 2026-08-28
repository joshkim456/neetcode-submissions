class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for r in range(len(position)):
            timeToTarget = (target - cars[r][0]) / cars[r][1]
            if not stack or timeToTarget > stack[-1]:
                stack.append(timeToTarget)
        
        return len(stack)
            
        
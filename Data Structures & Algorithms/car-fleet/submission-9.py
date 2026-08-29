class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sortd = sorted(zip(position, speed), reverse=True)

        for r in range(len(sortd)):
            timeToTarget = (target - sortd[r][0]) / sortd[r][1]
            if not stack or stack[-1] < timeToTarget:
                stack.append(timeToTarget)
            
        
        return len(stack)

[3]
        
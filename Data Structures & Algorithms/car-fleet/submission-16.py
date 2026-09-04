class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sortd = sorted(([position[i], speed[i]] for i in range(len(position))), reverse=True)
        
        for r in range(len(sortd)):
            timeToTarget = (target - sortd[r][0]) / sortd[r][1]
            if stack and stack[-1] >= timeToTarget:
                continue
            stack.append(timeToTarget)
        
        return len(stack)



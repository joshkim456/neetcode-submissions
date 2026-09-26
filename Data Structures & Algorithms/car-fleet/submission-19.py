class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        for r in range(len(position)):
            timeToTarget = (target - cars[r][0]) / cars[r][1]
            if not s or s[-1] < timeToTarget:
                s.append(timeToTarget)
        
        return len(s)



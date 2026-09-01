import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False

        d = {}
        h = []

        for n in hand:
            d[n] = d.get(n, 0) + 1
        
        for key, value in d.items():
            heapq.heappush(h, key)
        
        while h:
            first = h[0]

            for i in range(first, first+groupSize):
                if i not in d:
                    return False
                d[i] -= 1
                if d[i] == 0:
                    if i != h[0]:
                        return False
                    heapq.heappop(h)
        return True
            



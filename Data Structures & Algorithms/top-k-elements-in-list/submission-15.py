import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        h = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            heapq.heappush(h, (c, n))
            if len(h) > k:
                heapq.heappop(h)
        
        output = []
        for c, n in h:
            output.append(n)
        
        return output
        
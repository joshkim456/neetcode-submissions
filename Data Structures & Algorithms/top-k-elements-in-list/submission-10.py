class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        ans = []
        i = len(buckets)-1

        while i >= 0 and len(ans) < k:
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
            i -= 1

        return ans            
        


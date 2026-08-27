class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] =  freq.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        ans = []
        i = len(buckets) - 1
        while k > 0:
            if buckets[i] == []:
                i -= 1
            else:
                for n in buckets[i]:
                    ans.append(n)
                    k -= 1
                    if k == 0:
                        break
                i -= 1
        return ans
                
            
        


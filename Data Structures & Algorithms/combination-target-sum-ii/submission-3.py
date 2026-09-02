class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        candidates.sort()

        def dfs(i, total):
            if total == target: 
                res.append(cur.copy())
                return 
            if i >= len(candidates): return
            if total > target: return

            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            cur.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            i = j
            dfs(j, total)
        
        dfs(0, 0)
        return res

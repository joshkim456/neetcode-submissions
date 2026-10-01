class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates): return
            elif total > target: return

            cur.append(candidates[i])
            dfs(i+1, total+candidates[i])

            cur.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, total)

        dfs(0, 0)
        return res
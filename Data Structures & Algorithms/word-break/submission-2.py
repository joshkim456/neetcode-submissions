class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        words = set(wordDict)

        dp[0] = True 

        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        
        return dp[-1]

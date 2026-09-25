class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterCount = set()
        ans = 0
        i = 0
        j = 0

        while j < len(s):
            while s[j] in letterCount:
                letterCount.remove(s[i])
                i += 1

            letterCount.add(s[j])
            ans = max(ans, (j-i+1))
            j += 1
            
        return ans




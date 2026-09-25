class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        i = 0
        count = [0]*26

        for j in range(len(s)):
            count[ord(s[j])-65] += 1

            while (j-i+1)-max(count) > k:
                count[ord(s[i])-65] -= 1
                i += 1
            ans = max(ans, j-i+1)
        return ans

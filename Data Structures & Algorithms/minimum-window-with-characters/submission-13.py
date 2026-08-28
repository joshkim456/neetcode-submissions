class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = [0]*128
        sCount = [0]*128

        for letter in t:
            tCount[ord(letter)] += 1
        
        l = 0
        have = 0
        need = len(set(t))
        shortestLength = float('inf')
        ans = ""

        for r in range(len(s)):
            sCount[ord(s[r])] += 1
            if sCount[ord(s[r])] == tCount[ord(s[r])]:
                have += 1
            while have == need:
                if r-l+1 < shortestLength:
                    shortestLength = r-l+1
                    ans = s[l:r+1]
                
                sCount[ord(s[l])] -= 1
                if sCount[ord(s[l])] < tCount[ord(s[l])]:
                    have -= 1
                l += 1
        return ans

            
            




class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # maintain hashmap of count of charaters from a to z per sliding window
        # when you move sliding window, remove count from s2[l] and add s[r+1]
        # how do i efficiently compare char count in s1 against hashmap

        s1Count = [0]*26
        for s in s1:
            s1Count[ord(s)-97] += 1

        letterCount = [0]*26

        l = 0
        r = len(s1)-1

        for r in range(len(s2)):
            letterCount[ord(s2[r])-97] += 1
            if r >= len(s1):
                letterCount[ord(s2[r-len(s1)])-97] -= 1
            if letterCount == s1Count:
                return True
        return False

            

            




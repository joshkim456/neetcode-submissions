class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = [0]*26
        for letter in s1:
            s1Count[ord(letter)-97] += 1
        
        l = 0
        
        s2Count = [0]*26

        for r in range(len(s2)):
            s2Count[ord(s2[r])-97] += 1
            if r >= len(s1):
                s2Count[ord(s2[l])-97] -= 1
                l += 1
            if s1Count == s2Count:
                return True
        
        return False

          
        

            

            




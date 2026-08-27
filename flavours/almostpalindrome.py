from typing import List

class Solution:
    def almostPalindrome(self, s: str) -> bool:
        
        def isPalindrome(s):
            l = 0
            r = len(s)-1

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        l = 0
        r = len(s)-1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1])
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        i = 0
        j = len(s)-1

        valid = True

        while i <= j and valid:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                valid = False
        return valid
                
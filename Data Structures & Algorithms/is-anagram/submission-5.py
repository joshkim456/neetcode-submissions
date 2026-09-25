class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        for letter in s:
            sCount[letter] = sCount.get(letter, 0) + 1
        
        for letter in t:
            tCount[letter] = tCount.get(letter, 0) + 1
        
        return sCount == tCount
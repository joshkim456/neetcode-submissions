class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "." + s
        return encoded
        
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            length = ""
            j = i
            while s[j] != '.':
                length += s[j]
                j += 1
            length = int(length)

            strs.append(s[j+1:j+1+length])
            i = j+1+length
        return strs
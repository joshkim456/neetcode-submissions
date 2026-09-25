class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += str(len(s)) + "." + s
        
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            temp = ""

            while s[i].isdigit():
                temp += s[i]
                i += 1
            length = int(temp)
            i += 1

            newStr = ""
            while length > 0:
                newStr += s[i]
                i += 1
                length -= 1
            output.append(newStr)

        return output
            




            
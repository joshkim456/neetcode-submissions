class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #maintain array of letter counts within window
        #maintain array of l and r answer indices
        #you only start the window (searching before) at a letter that is inside t
        
        l = 0
        r = 0

        tCount = [0]*128
        for letter in t:
            tCount[ord(letter)] += 1

        letterCount = [0]*128
        viable = False

        indices = []
        have = 0
        need = len(set(t))

        while r < len(s):
            while not viable and r < len(s):
                if s[r] in t:
                    letterCount[ord(s[r])] += 1
                    if letterCount[ord(s[r])] == tCount[ord(s[r])]:
                        have += 1
                if have == need:
                    indices.append([l, r])
                    viable = True
                r += 1
            
            while viable:
                if s[l] in t:
                    letterCount[ord(s[l])] -= 1
                    if letterCount[ord(s[l])] < tCount[ord(s[l])]:
                        have -= 1
                l += 1

                if have != need:
                    viable = False
                else:
                    indices.append([l, r-1])

        
        minLength = 10000000
        ansL = 0
        ansR = 0
        for pair in indices:
            if pair[1] - pair[0] < minLength:
                minLength = pair[1] - pair[0]
                ansL = pair[0]
                ansR = pair[1]
        if indices == []:
            return ""
        return s[ansL:ansR+1]
            




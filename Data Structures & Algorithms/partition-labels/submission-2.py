class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        output = []
        
        # start at 0, find the new max index to go to
        # traverse the letters from start to max index, if a new max index comes along, then increase max index to that new max
        # stop when you reach, so while index < maxIndex
        # new index after is index + 1

        index = 0

        while index < len(s):
            length = 1
            maxIndex = last[s[index]]

            while index < maxIndex:
                maxIndex = max(maxIndex, last[s[index]])
                index += 1
                length += 1
            output.append(length)
            index += 1
        
        return output
            
        
        
            
    


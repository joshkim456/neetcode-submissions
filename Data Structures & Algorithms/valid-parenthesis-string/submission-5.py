class Solution:
    def checkValidString(self, s: str) -> bool:
        mini = 0
        maxi = 0

        for letter in s:
            if letter == "(":
                mini += 1
                maxi += 1
            elif letter == ")":
                mini = mini - 1
                if mini < 0: mini = 0
                maxi -= 1
                if maxi < 0: return False
            else:
                mini = mini - 1
                if mini < 0: mini = 0
                maxi += 1
        
        return mini == 0

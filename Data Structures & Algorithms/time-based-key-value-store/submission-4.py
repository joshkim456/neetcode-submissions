class TimeMap:

    def __init__(self):
            self.hashmap = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
            if key in self.hashmap:
                self.hashmap[key].append((timestamp, value))
            else:
                self.hashmap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
            if key in self.hashmap:
                lo = 0
                hi = len(self.hashmap[key])-1
                best = ""

                while lo <= hi:
                    mid = (lo + hi) // 2
                    if self.hashmap[key][mid][0] <= timestamp:
                        best = self.hashmap[key][mid][1]
                        lo = mid + 1
                    else:
                        hi = mid - 1
                return best
            return ""
                    
                
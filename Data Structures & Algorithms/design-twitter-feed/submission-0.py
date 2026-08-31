import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.relationships = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId in self.relationships:
            for followee in self.relationships[userId]:
                for t, tid in self.tweets.get(followee, [])[-10:]:
                    heapq.heappush(feed, (-t, tid))
        
        if userId in self.tweets:
            for t, tid in self.tweets[userId][-10:]:
                    heapq.heappush(feed, (-t, tid))
        
        ans = []
        while len(ans) < 10 and feed:
            ans.append(heapq.heappop(feed)[1])
        return ans

        
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.relationships.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.relationships:
            self.relationships[followerId].discard(followeeId)
        
    

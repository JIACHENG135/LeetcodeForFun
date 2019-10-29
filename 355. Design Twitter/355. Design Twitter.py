from collections import defaultdict
from heapq import merge
class Twitter:

    def __init__(self):
        self.userMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time -= 1
        self.tweetMap[userId].append([self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:

        followee = self.userMap[userId]
        followee.add(userId)
        candidates = [reversed(self.tweetMap[u]) for u in followee]
        twt = []
        for t in merge(*candidates):
            twt.append(t[1])
            if len(twt)==10:
                return twt
        return twt
    def follow(self, followerId: int, followeeId: int) -> None:

        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.userMap[followerId].discard(followeeId)

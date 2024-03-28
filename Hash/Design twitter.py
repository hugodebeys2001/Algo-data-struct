from collections import defaultdict
from heapq import merge


class Tweet:
    def __init__(self, tweetId, timestamp):
        self.tweetId = tweetId
        self.timestamp = timestamp

    # Define comparison method
    def __lt__(self, other):
        return self.timestamp < other.timestamp


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # User ID -> List of Tweets
        self.followees = defaultdict(set)  # User ID -> Set of Followees

        # Timestamp for tweets
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append(Tweet(tweetId, self.timestamp))

    def getNewsFeed(self, userId: int):
        # Merge tweets from user and followees
        tweets = merge(*[self.tweets[u] for u in (userId, *self.followees[userId])])

        # Reverse the order of tweets and select the first 10
        tweets = reversed(list(tweets))
        return [tweet.tweetId for _, tweet in zip(range(10), tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
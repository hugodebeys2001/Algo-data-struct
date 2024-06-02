#https://www.geeksforgeeks.org/problems/design-twitter/0

from collections import defaultdict
from heapq import merge


class Tweet:
    def __init__(self, tweetId, timestamp):
        self.tweetId = tweetId
        self.timestamp = timestamp

    # Defini la éthode de comparison
    def __lt__(self, other):
        return self.timestamp < other.timestamp


class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # User ID -> Liste des Tweets
        self.followees = defaultdict(set)  # User ID -> Sets des Followees


        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append(Tweet(tweetId, self.timestamp))

    def getNewsFeed(self, userId: int):
        # Récupérer les tweets de l'utilisateur
        user_tweets = self.tweets[userId]

        # Récupérer les tweets de chaque followee
        followees_tweets = [self.tweets[u] for u in self.followees[userId]]

        all_tweets = [user_tweets] + followees_tweets

        # Fusionner toutes les listes de tweets triés
        merged_tweets = merge(*all_tweets)

        # Inverser l'ordre des tweets
        tweets = reversed(list(merged_tweets))

        # Créer une liste vide pour les identifiants des tweets
        tweet_ids = []

        # Utiliser zip pour itérer simultanément sur les indices et les tweets
        for _, tweet in zip(range(10), tweets):
            tweet_ids.append(tweet.tweetId)

        # Retourner la liste des identifiants des tweets
        return tweet_ids

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

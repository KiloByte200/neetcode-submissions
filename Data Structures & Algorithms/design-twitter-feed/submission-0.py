import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.timestamp = 0

        # userId -> [(timestamp, tweetId), ...]
        self.tweets = defaultdict(list)

        # followerId -> {followeeId, ...}
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # Include the user and everyone they follow.
        relevant_users = self.following[userId] | {userId}

        # Add each relevant user's newest tweet.
        for user in relevant_users:
            if not self.tweets[user]:
                continue

            tweet_index = len(self.tweets[user]) - 1
            timestamp, tweet_id = self.tweets[user][tweet_index]

            heapq.heappush(
                heap,
                (-timestamp, tweet_id, user, tweet_index)
            )

        news_feed = []

        while heap and len(news_feed) < 10:
            _, tweet_id, user, tweet_index = heapq.heappop(heap)
            news_feed.append(tweet_id)

            # Add this user's next-newest tweet.
            previous_index = tweet_index - 1

            if previous_index >= 0:
                timestamp, previous_tweet_id = self.tweets[user][previous_index]

                heapq.heappush(
                    heap,
                    (-timestamp, previous_tweet_id, user, previous_index)
                )

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
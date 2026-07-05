class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follows[userId].add(userId)
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_tweets = []
        for followee_id in self.follows[userId]:
            feed_tweets.extend(self.tweets[followee_id])
        
        feed_tweets.sort(key=lambda x: -x[0])
        return [tweet_id for _, tweet_id in feed_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follows[userId].add(userId) # follow my self

        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft
        
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_tweets = []
        for profiles in self.follows[userId]:
            for tweet in self.tweets[profiles]:
                feed_tweets.append(tweet)
        # for tweet in self.tweets[userId]:
        #         feed_tweets.append(tweet)
        
        feed_tweets.sort(key=lambda x: -x[0])

        length = min(10, len(feed_tweets))
        feed_tweets = feed_tweets[:length]

        result = list(map(lambda x : x[1], feed_tweets))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.follows[followerId].discard(followeeId)











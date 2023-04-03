import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:TheKnowledgeHou) until:2023-04-01 since:2020-04-01"
tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.viewCount])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Likes', 'Comments', 'Retweets','Views'])

# to save to csv
df.to_csv('data/tweets.csv')
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
consumer_key = 'lpLqgvGrLTB4gvO2PmLRvTvFm'
consumer_secret = '27sM0qdMroK7BGg7LQIAHEPV6KWj2O5EYOLMM9o9lmF4vLKnve'
access_token = '3237679314-J3JDs0zlteJnBU3UO6NjYr5XhpSheyD2cKuh7uC'
access_token_secret = 'k0f76CbAkcGU9S6n8derZdO7i5heQen2fySMPJ5k9c8kL'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
# # extracting the tweets from the # and iterating over it
# for tweet in tweepy.Cursor(api.search, q='#ShaheedDiwas', rpp=100).items():
#     print(tweet.text)
#     print(tweet.created_at)
#     break



# tweet="Tributes to Shaheed Bhagat Singh, Rajguru and Sukhdev #ShaheedDiwas "
# api.update_status(status=tweet)

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
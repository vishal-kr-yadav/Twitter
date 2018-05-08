import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

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

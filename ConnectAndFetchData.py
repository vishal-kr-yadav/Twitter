import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import configparser

# Reading the configurations from the config file
config = configparser.ConfigParser()
config.sections()
config.read('./config.ini')

consumer_key = config['twitter_credentials']['consumer_key']
consumer_secret = config['twitter_credentials']['consumer_secret']
access_token = config['twitter_credentials']['access_token']
access_token_secret = config['twitter_credentials']['access_token_secret']



class StdOutListener(StreamListener):

    def on_data(self, data):
        # tweets will come within the data part
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
    stream.filter(track=['IPL'])
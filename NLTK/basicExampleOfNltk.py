# https://www.digitalocean.com/community/tutorials/how-to-work-with-language-data-in-python-3-using-the-natural-language-toolkit-nltk
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents

tweets=twitter_samples.strings('positive_tweets.json')
tweets_tokens=twitter_samples.tokenized('positive_tweets.json')
tweets_tokenzied=pos_tag_sents(tweets_tokens)
print(tweets_tokenzied)


JJ_count=0
NN_count=0

for tweet in tweets_tokenzied:
    # print("===",tweet)

    for pair in tweet:
        tag=pair[1]
        if tag=='JJ':
            JJ_count+=1
        elif tag=='NN':
            NN_count+=1


print('NN count==',NN_count)
print('JJ_count==',JJ_count)
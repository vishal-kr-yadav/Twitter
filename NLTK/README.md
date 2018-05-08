Information Regarding **basicExampleOfNltk.py**
Reference :https://www.digitalocean.com/community/tutorials/how-to-work-with-language-data-in-python-3-using-the-natural-language-toolkit-nltk

### Installation
pip install nltk


### tweets=twitter_samples.strings('positive_tweets.json')   

When we first load our list of tweets, each tweet is represented as one string. Before we can determine which words in our tweets are adjectives or nouns, we first need to tokenize our tweets.


**Tokenization** is the act of breaking up a sequence of strings into pieces such as words, keywords, phrases, symbols and other elements, which are called tokens. Let's create a new variable called tweets_tokens, to which we will assign the tokenized list of tweets

 Now that we have the tokens of each tweet we can tag the tokens with the appropriate POS tags.
 
 In NLTK, the abbreviation for adjective is JJ
 
 NLTK tagger marks singular nouns (NN) with different tags than plural nouns (NNS). To simplify, we will only count singular nouns by keeping track of the NN tag
 
 
 **Counting POS Tags**
 We will keep track of how many times JJ and NN appear using an accumulator (count) variable, which we will continuously add to every time we find a tag.
 
**====================================================**

## basicOperationWithTwitterApi.py

->it contains some basic operation like i)retrieve data using hashtag ii)post a tweet using the API

**====================================================**
## Analyzing_tweets.py

Befor using the scripts:
create "twitter_data.csv" file using the basicOperationWithTwitterApi.py.You just need to append the tweet into this file


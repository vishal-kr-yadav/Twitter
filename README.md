###First Step:
create a twitter app: i)log into :https://apps.twitter.com/
 ii)create new app
 iii)get your credentials from the app
 Reference link :https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
 
 ####Second Step
 **setup the installation**:
  $pip install tweepy  
  ***Note***:Tweepy is an open-source and easy-to-use library that allows your Python programming projects to access the Twitter API.
     
###Final Step
**Fetch data fo hashtag(#)"""
i)edit the ***ConnectAndFetchData.py***  
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

ii)open the script and mention your hastag within  
**stream.filter(track=['your_hastag'])**

iii)Run
python3 ConnectAndFetchData.py   or python ConnectAndFetchData
depending upon your environment

**NOTE** i have not hard coded the all twitter key within the programs.I have maintain a config.ini file where i have mention my credentials  
i)create a config.ini file and mention
         **consumer_key = ''  
            consumer_secret = ''  
            access_token = ''  
            access_token_secret = ''**
            
In the main ConnectAnndFetchData.py w have reading the config.ini .So you dont need to worry about that
            




  
 

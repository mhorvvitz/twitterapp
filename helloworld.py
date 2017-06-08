import tweepy
import time

#create variables for each key, secret and token
consumer_key = "jRM6cXxZUdlT6l33z0S4TPX6o"
consumer_secret = "UevkzIvwRv7AvXQGKh7fl9fNlRHqd1nZXuBcIKtwvq0mouNDw0"
access_token = "430397353-VyvpvWTwICtC0VsEzZCWuINh8WuyJb3ZgCSYQxq0"
access_token_secret = "8pCGYx6kOYpEyR8hzkUxLqRvbt7EPO0CPehsBxTi1VOhb"

#set up OAuth and integrate with API
auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api =tweepy.API(auth)

followers = ()

followers = api.followers('gocoderz')

screen_names = ()
screen_names = (follower['screen_name'] for follower in followers)

print screen_names

followers_string = str(screen_names)
followers_file = open("follower_list", "w")
followers_file.write(followers_string)

print "done"




#enter acount name
#account_name = raw_input("Account name: ")


#rate limit handling, twitter api limits 15 calls to every 15 minutes
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

#loop through followers and print their screen names
#for follower in limit_handled(tweepy.Cursor(api.followers, id="gocoderz").items(3)):
 #  print follower.screen_name
  
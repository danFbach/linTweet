import tweepy
from tweepy import OAuthHandler

consumer_key = 'h6oWUxM94nHOhCwN513qZx7J6'
consumer_secret = '6GLzL5ILL8iI0HV2VqLWCJVLlfuM2AfWgyykmI1rIc3HE6GgUx'
access_token = '3014229268-jdGmGCouZWJbpuPM2VPcFKaHsznXBwOvYSK6K2K'
access_secret = 'ouy8engsBch1Io0gx5ZaC5gyNKklt4dYHCdTlEaSwE8C5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.SearchResults(api.search('Asus')):
    # Process a single status
    print(status)
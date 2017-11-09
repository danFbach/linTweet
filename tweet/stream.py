import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

consumer_key = 'h6oWUxM94nHOhCwN513qZx7J6'
consumer_secret = '6GLzL5ILL8iI0HV2VqLWCJVLlfuM2AfWgyykmI1rIc3HE6GgUx'
access_token = '3014229268-jdGmGCouZWJbpuPM2VPcFKaHsznXBwOvYSK6K2K'
access_secret = 'ouy8engsBch1Io0gx5ZaC5gyNKklt4dYHCdTlEaSwE8C5'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(StreamListener):
    count = 0

    def on_data(self, data):
        try:
            with open('tmo.json', "a") as f:
                print(self.count, data)
                f.write(data)
                self.count += 1
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#pbach123'])
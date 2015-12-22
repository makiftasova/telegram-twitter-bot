#!/user/bin/env python3
import common

import os
import sys

import json
import bot
import tweepy
from stream import TweetsStreamListener

def main():

	print("Booting")

	common.init()

	telegram_bot_token=""
	twitter_consumer_key=""
	twitter_consumer_secret=""
	twitter_access_token=""
	tiwtter_access_secret=""

	# READ API TOKENS FROM FILE
	with open('tokens.json') as token_file:
		token_data = json.load(token_file)
		telegram_bot_token = token_data['telegram_bot_token']
		twitter_consumer_key = token_data['consumer_key']
		twitter_consumer_secret = token_data['consumer_secret']
		twitter_access_token = token_data['access_token']
		tiwtter_access_secret = token_data['access_token_secret']

	follow_list = []
	with open('follow_list.json') as follow_list_file:
		follow_data = json.load(follow_list_file)
		follow_list = follow_data['follow_list']

	#AUTH
	auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
	auth.set_access_token(twitter_access_token, tiwtter_access_secret)

	api = tweepy.API(auth)

	follow_list_ids = []
	for item in follow_list:
		user = api.get_user(item)
		follow_list_ids.append(str(user.id))

	stream = ""
	try:
		#SET UP STREAM
		streamListener = TweetsStreamListener()
		stream = tweepy.Stream(auth=api.auth, listener=streamListener)
		stream.filter(follow=follow_list_ids, async=True)
		bot.bot_main(telegram_bot_token)
	except KeyboardInterrupt:
		print("KeyboardInterrupt")
		stream.disconnect()
		print("Disconnected from stream")
		#sys.exit(0)

if __name__ == "__main__":
	main()
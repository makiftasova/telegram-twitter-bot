#!/user/bin/env python3

import os

import telegram
import json


def init():
	global subscribers
	if os.path.isfile('subcribers.json'):
		subscribers = loadSubscribers()
	else:
		subscribers = []
	global bot
	bot = ""

def saveSubscribers(subscribers_list):
	with open('subcribers.json', 'w') as subcribers_list_file:
		save_data = {'subcribers' : subscribers_list}
		json.dump(save_data, subcribers_list_file)

def loadSubscribers():
	with open('subcribers.json') as subcribers_list_file:
		load_data = json.load(subcribers_list_file)
		return load_data['subcribers']
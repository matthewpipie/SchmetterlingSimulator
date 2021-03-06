#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
import json
import time
import random

wordDictFile = open("wordDict.txt", "r")
startWordsFile = open("startWords.txt", "r")

print "loading 1..."
wordDict = json.load(wordDictFile)
print "loading 2..."
startWords = json.load(startWordsFile)

wordDictFile.close()
startWordsFile.close()


def genWord():
	prevWord = random.choice(startWords)
	msg = prevWord + " "

	while prevWord != "\n":
		prevWord = random.choice(wordDict[prevWord])
		msg += prevWord + " "
		if random.randint(0, 50) == 0:
			break
		if len(msg.split()) < 3 and random.randint(0,1) == 0 and prevWord == '\n':
			continue

	return msg.replace(u"@", u"@​")


def simulate(bot, update):
        print "sending"
	msg = genWord()
        print "msg: " + msg
	bot.send_message(chat_id=update.message.chat_id, text=msg)
	print "sent"

if __name__ == "__main__":
	tokenFile = open("token.txt", "r")
	print "loading 3..."
	updater = Updater(token=tokenFile.read().replace('\n', ''))
	tokenFile.close();
	dispatcher = updater.dispatcher
	startHandler = CommandHandler('simulate', simulate)
	dispatcher.add_handler(startHandler)
	print "starting"
	updater.start_polling()
	updater.idle()

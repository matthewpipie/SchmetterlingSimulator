from telegram.ext import Updater
from telegram.ext import CommandHandler
import json
import random

wordDictFile = open("wordDict.txt", "r")
startWordsFile = open("wordDict.txt", "r")

wordDict = json.read(wordDictFile)
startWords = json.read(startWordsFile)

wordsDictFile.close()
startWordsFile.close()


def genWord():
	prevWord = random.choice(startWords)
	msg = prevWord + " "

	while prevWord != "\n":
		prevWord = random.choice(wordDict[prevWord])
		msg += prevWord + " "
		if random.randint(0, 50) == 0:
			break;

	return msg.replace("@", "@​")


def simulate(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=genWord())

if __name__ == "__main__":
	tokenFile = open("token.txt", "r")
	updater = Updater(token=tokenFile.read().replace('\n', ''))
	tokenFile.close();
	dispatcher = updater.dispatcher
	startHandler = CommandHandler('simulate', simulate)
	dispatcher.add_handler(startHandler)
	updater.start_polling()
	#while True:
	#	chatID = bot.getUpdates()[-1].message.chat_id
	#	bot.sendMessage(chat_id=chat_id, text=genWord())

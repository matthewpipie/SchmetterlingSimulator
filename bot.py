import telegram
import json
import random

log = open("Schmetterling.jsonl", "r")
a = 0;
wordDict = {}
startWords = []
for line in log:
	a += 1;
	test = json.loads(line)
	if 'text' in test:
		text = json.loads(line)['text']

		prevWord = text.split()[0]
		startWords.append(prevWord)

		for word in text.split()[1:] + ['\n']:
			if (prevWord in wordDict):
				wordDict[prevWord].append(word)
			else:
				wordDict[prevWord] = [word]

			prevWord = word
	if (a % 1000) == 0:
		print a
	if a == 10000:
		pass
		#break


def genWord():
	prevWord = random.choice(startWords)
	msg = prevWord + " "

	while prevWord != "\n":
		prevWord = random.choice(wordDict[prevWord])
		msg += prevWord + " "
		if random.randint(0, 50) == 0:
			break;
	
	return msg.replace("@", "@*")




if __name__ == "__main__":
	tokenFile = open("token.txt", "r")
	bot = telegram.Bot(token=tokenFile.read())
	tokenFile.close();
	while True:
		chatID = bot.getUpdates()[-1].message.chat_id
		bot.sendMessage(chat_id=chat_id, text=genWord())
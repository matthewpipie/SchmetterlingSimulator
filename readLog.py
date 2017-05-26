import json
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

f1 = open("startWords.txt", "w")
json.dump(startWords, f1)
f1.close()
f2 = open("wordDict.txt", "w")
json.dump(wordDict, f2)
f2.close()


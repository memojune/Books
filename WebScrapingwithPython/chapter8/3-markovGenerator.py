from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')

    punctuation = [',', '.', ';', ':']
    for symble in punctuation:
        text = text.replace(symble, ' '+symble+' ')

    words = text.split(' ')
    words = list(filter(lambda x: x!='', words))

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1
    return wordDict

text = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read().decode('utf-8')
wordDict = buildWordDict(text)

length = 100
chain = ''
currentWord = 'I'
for i in range(length):
    chain += currentWord+' '
    currentWord = retrieveRandomWord(wordDict[currentWord])
print(chain)
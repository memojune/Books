import nltk, re
from nltk import word_tokenize
from nltk.corpus import gutenberg, nps_chat
from nltk.corpus import brown

# 网络获取文本 可使用BeautifulSoup
from urllib import request
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw = response.read().decode('utf-8')
print(raw[:75])
tokens = word_tokenize(raw)
print(tokens[:10])
text = nltk.Text(tokens)

# 本地
'''
with open(path) as f:
    raw = f.read()
    # next...
'''

# 正则
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

# 搜索已分词文本
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print(moby.findall(r'<a> (<.*>) <man>'))
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
print(hobbies_learned.findall(r'<as> <\w*> <as> <\w*>'))

# 词干提取器
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
print([porter.stem(t) for t in tokens])
print([lancaster.stem(t) for t in tokens])

# 词性归并
wnl = nltk.WordNetLemmatizer()
print([wnl.lemmatize(t) for t in tokens])



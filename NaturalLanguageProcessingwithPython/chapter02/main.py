import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

# Gutenberg语库文件
print(gutenberg.fileids())
# 获得'austen-emma.txt'
emma = gutenberg.words('austen-emma.txt')
# 打印Gutenberg语库文件信息
for fileid in gutenberg.fileids():
    # 字符数
    num_chars = len(gutenberg.raw(fileid))
    # 词数
    num_words = len(gutenberg.words(fileid))
    # 句数
    num_sents = len(gutenberg.sents(fileid))
    # 词数（去重）
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents),
          round(num_words/num_vocab), fileid)

# Brown语料库
print(brown.categories())
# （文体，单词）
cfd = nltk.ConditionalFreqDist((genre, word)
                               for genre in brown.categories()
                               for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
# 打印（文体，单词）分布
cfd.tabulate(conditions=genres, samples=modals)

# 随机生成文本
def generate_model(cfdist, word, num=15):
    # cfdist来自于某文本
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

# 停用词，即高频词汇
print(stopwords.words('english'))

# 同义词集
print(wn.synsets('motorcar'))
# 'car.n.01'同义词集中的词
print(wn.synset('car.n.01').lemma_names())
# 定义
print(wn.synset('car.n.01').definition())
# 示例
print(wn.synset('car.n.01').examples())
# 词条
print(wn.synset('car.n.01').lemmas())
# 找到同义词集
print(wn.lemma('car.n.01.automobile').synset())






import nltk
from nltk.corpus import brown

# 分词&标注词性
text = nltk.word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

# str to tuple
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token) # ('fly', 'NN')

# 已标注文本
print(brown.tagged_words())
print(brown.tagged_words(tagset='universal')) # 简化的词性标注

brown_news_tagged = brown.tagged_words(categories='news',
                                       tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print(tag_fd.most_common())
# tag_fd.plot(cumulative=True)

# 新闻中最常见的动词
wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
print([wt[0] for (wt, _) in word_tag_fd.most_common()
                                    if wt[1]=='VERB'])

# 找出最频繁的名词标记
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag)
                                   in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

tagdict = findtags('NN', brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
    print(tag, tagdict[tag])

# often后的词
brown_learned_text = brown.words(categories='learned')
print(sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text)
                 if a == 'often')))
# often后的词性
brown_lrnd_tagged = brown.tagged_words(categories='learned',
                                       tagset='universal')
tags = [b[1] for (a, b) in nltk.bigrams(brown_lrnd_tagged)
                                        if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()

# 及特定标记和词序列的词 'verb to verb'
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1, w2, w3)
for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

# 词性标注
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents)*0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train=train_sents, backoff=t0)
t2 = nltk.BigramTagger(train=train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train=train_sents, backoff=t2)
print(t3.evaluate(test_sents))






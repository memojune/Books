import nltk
from nltk.corpus import brown
from nltk.corpus import conll2000
import re

# 分句-分词-词性标注
def ie_preprocess(document):
    sents = nltk.sent_tokenize(document)
    sents = [nltk.word_tokenize(sent) for sent in sents]
    sents = [nltk.pos_tag(sent) for sent in sents]
    return sents

# 名词短语分块
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
            ("the", "DT"), ("cat", "NN")]
grammar = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(grammar)
res = cp.parse(sentence)
print(res)

# 搜索文本
cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == 'CHUNK':
            print(subtree)

# 加缝
grammar = '''NP: {<.*>+} 
                 }<VBD|IN>+{'''
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
            ("the", "DT"), ("cat", "NN")]
cp = nltk.RegexpParser(grammar)
print(cp.parse(sentence))

# CoNLL2000 分块语料
print(conll2000.chunked_sents('train.txt')[99])

# 使用unigram标注器对名词短语分块
# 将unigram改为bigram标注效果更好
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c
                       in nltk.chunk.tree2conlltags(sent)]
                       for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos = self.tagger.tag(pos_tags)
        chunktages = [chunktag for (pos, chunktag) in tagged_pos]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag)
                     in zip(sentence, chunktages)]
        return nltk.chunk.conlltags2tree(conlltags)
# 训练-测试
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
unigram_chunker = UnigramChunker(train_sents)
print(unigram_chunker.evaluate(test_sents))

# 级联分块器
grammar = r"""
  NP: {<DT|JJ|NN.*>+}
  PP: {<IN><NP>}
  VP: {<VB.*><NP|PP|CLAUSE>+$}
  CLAUSE: {<NP><VP>}
  """
cp = nltk.RegexpParser(grammar, loop=2) # 重复两次，避免未识别块
sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"),
            ("cat", "NN"), ("sit", "VB"), ("on", "IN"),
            ("the", "DT"), ("mat", "NN")]
print(cp.parse(sentence))

# 树
tree1 = nltk.Tree('NP', ['Alice'])
tree2 = nltk.Tree('NP', ['the', 'rabbit'])
tree3 = nltk.Tree('VP', ['chased', tree2])
tree4 = nltk.Tree('S', [tree1, tree3])
print(tree4)
tree4.draw()

# 关系抽取
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,
                                     corpus='ieer', pattern = IN):
        print(nltk.sem.rtuple(rel))








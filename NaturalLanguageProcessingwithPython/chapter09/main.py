import nltk
from nltk import load_parser

# 基于特征的文法
nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')

# 跟踪基于特征的图表分析器
tokens = 'Kim likes children'.split()
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)
for tree in cp.parse(tokens):
    print(tree)

# 构造特征结构
fs1 = nltk.FeatStruct(PER=3, NUM='pl', GND='fem')
print(fs1)
fs1['CASE'] = 'acc'
fs2 = nltk.FeatStruct(POS='N', AGR=fs1)
print(fs2)

print(nltk.FeatStruct("[POS='N', AGR=[PER=3, NUM='pl', GND='fem']]"))
print(nltk.FeatStruct(NAME='Lee', TELNO='01 27 86 42 96', AGE=33))

# 结构共享
print(nltk.FeatStruct("""[NAME='Lee', 
                          ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'], 
                          SPOUSE=[NAME='Kim', ADDRESS->(1)]]"""))
print(nltk.FeatStruct("[A='a', B=(1)[C='c'], D->(1), E->(1)]"))

# 统一
fs1 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')
fs2 = nltk.FeatStruct(CITY='Paris')
print(fs1.unify(fs2))

# 结构共享使用变量表示
fs1 = nltk.FeatStruct("[ADDRESS1=[NUMBER=74, STREET='rue Pascal']]")
fs2 = nltk.FeatStruct("[ADDRESS1=?x, ADDRESS2=?x]")
print(fs2)
print(fs2.unify(fs1))

# 具有倒装从句和长距离依赖的产生式的文法
nltk.data.show_cfg('grammars/book_grammars/feat1.fcfg')
tokens = 'who do you claim that you like'.split()
cp = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in cp.parse(tokens):
    print(tree)
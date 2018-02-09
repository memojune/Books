import nltk
from nltk import load_parser

# sql文法
nltk.data.show_cfg('grammars/book_grammars/sql0.fcfg')
cp = load_parser('grammars/book_grammars/sql0.fcfg')
query = 'What cities are located in China'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)

# ASCII版本运算符
nltk.boolean_ops()

# 将逻辑表达式分析成表达式
read_expr = nltk.sem.Expression.fromstring
print(read_expr('-(P & Q)'), read_expr('P & Q'),
      read_expr('P | (R -> Q)'), read_expr('P <-> -- P'), sep='\n')

# 定理证明pover9
# lp = nltk.sem.Expression.fromstring
# SnF = read_expr('SnF')
# NotFnS = read_expr('-FnS')
# R = read_expr('SnF -> -FnS')
# prover = nltk.Prover9()
# prover.prove(NotFnS, [SnF, R])

# 真值模型
dom = {'b', 'o', 'c'}
v = '''
    bertie => b
    olive => o
    cyril => c
    boy => {b}
    girl => {o}
    dog => {c}
    walk => {o, c}
    see => {(b, o), (c, b), (o, c)}
'''
val = nltk.Valuation.fromstring(v)
print(val)
g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
print(g)
m = nltk.Model(dom, val)
print(m.evaluate('see(olive, y)', g))
print(m.evaluate('see(y, x)', g))

# 量化
print(m.evaluate('exists x.(girl(x) & walk(x))', g))
print(m.evaluate('girl(x) & walk(x)', g.add('x', 'o')))

# 满足公式的所有个体
fmla1 = read_expr('girl(x) | boy(x)')
print(m.satisfiers(fmla1, 'x', g))
fmla2 = read_expr('girl(x) -> walk(x)')
print(m.satisfiers(fmla2, 'x', g))
fmla3 = read_expr('walk(x) -> girl(x)')
print(m.satisfiers(fmla3, 'x', g))




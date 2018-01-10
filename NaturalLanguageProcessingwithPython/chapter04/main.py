'''
这章主要讨论了python程序编写，故大多略去
这里主要实现一个通过迭代、自下而上动态规划、自上而下动态规划以及@memoize
3种方法解决问题的程序

问题：
    S占1个长度单位，L占2个长度单位，列出长度为n的序列的所有排序
'''

# 迭代
def virahankal1(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['S']
    else:
        s = ['S' + prosody for prosody in virahankal1(n-1)]
        l = ['L' + prosody for prosody in virahankal1(n-2)]
        return s + l

# 自下而上动态规划
def virahankal2(n):
    lookup = ['', 'S']
    for i in range(n-1):
        s = ['S' + prosody for prosody in lookup[i+1]]
        l = ['L' + prosody for prosody in lookup[i]]
        lookup.append(s+l)
    return lookup[n]

# 自上而下动态规划
def virahankal3(n, lookup={0:[''], 1:['S']}):
    if n not in lookup:
        s = ['S' + prosody for prosody in lookup[i + 1]]
        l = ['L' + prosody for prosody in lookup[i]]
        lookup[n] = s + l
    return lookup[n]

# @memoize：存储函数调用结果，遇见相同参数的函数调用时免去重复计算
from nltk import memoize
@memoize
def virahanka4(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["S"]
    else:
        s = ["S" + prosody for prosody in virahanka4(n-1)]
        l = ["L" + prosody for prosody in virahanka4(n-2)]
        return s + l










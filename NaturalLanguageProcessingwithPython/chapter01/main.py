from nltk.book import *

print(text1)
print(text2)

# 搜索文本
text1.concordance('monstrous')
# 出现在与'monstrous'相似上下文的词
text1.similar('monstrous')
text2.similar('monstrous')
# 两个或两个以上的词共同的上下文
text2.common_contexts(["monstrous", "very"])
# 词的分布
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
# 按频率降序输出双连词
text4.collocations()

# FreqDist
fdist1 = FreqDist(text1)
print(fdist1)
# 50个最常出现的词
fdist1.most_common(50)
# 最常出现的词
w = fdist1.max()
# 出现次数
print(fdist1[w])
# 出现频率
print(fdist1.freq(w))
# 频率分布表
fdist1.tabulate()


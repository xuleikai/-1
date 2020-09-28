#关键词提取
from snownlp import SnowNLP
a = input ("输入文本：")
s = SnowNLP('a')
print(s.sentiments)

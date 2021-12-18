import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.casual import casual_tokenize
from nltk.util import ngrams

sentence="""Thomas Jefferson began building Monticello at the age of 26."""
tokenizer=RegexpTokenizer(r'\w+|$[0-9.]+|\S+')
print(tokenizer.tokenize(sentence))

#该分词器有利于NLP流水线的后续步骤，如词干还原
sentence="""Monticello wasn't designed as UNESCO World Heritage Site until 1987."""
tokenizer=TreebankWordTokenizer()
print(tokenizer.tokenize(sentence))

#该分词器用于处理来自社交网络的非规范的包含表情符号的短文本
message="""RT @TJMonticello Best day everrrrrr at Monticello.
Awesommmmmmeeeeeeee day :*)"""
casual_tokenize(message)
print(casual_tokenize(message,reduce_len=True,strip_handles=True))

#原始的1-gram分词器
sentence="""Thomas Jefferson began building Monticello at the age of 26."""
pattern=re.compile(r"([\s.,;!?])+")
tokens=pattern.split(sentence)
tokens=[x for x in tokens if x and x not in '- \t\n.,;!?']
print(tokens)

print(list(ngrams(tokens,2)))
print(list(ngrams(tokens,3)))

#元组变成字符串
two_grams=list(ngrams(tokens,2))
three_grams=list(ngrams(tokens,3))
print([" ".join(x) for x in two_grams])
print([" ".join(x) for x in three_grams])





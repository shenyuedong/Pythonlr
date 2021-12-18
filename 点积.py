import pandas as pd
import regex
import nltk
import nlpia

v1=pd.np.array([1,2,3])
v2=pd.np.array([2,3,4])
print(v1.dot(v2))
print((v1*v2).sum())
print(sum([x1*x2 for x1,x2 in zip(v1,v2)]))

stopwords=nltk.corpus.stopwords.words('english')
print(stopwords)

import nltk
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words

#stop_words=['a','an','the','on','of','off','this','is']
#tokens=['the','house','is','on','fire']
#tokens_without_stopwords=[x for x in tokens if x not in stop_words]
#print(tokens_without_stopwords)
#import nltk
#import ssl
#try:
 #   _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
 #   pass
#else:
 #   ssl._create_default_https_context = _create_unverified_https_context

#nltk.download('stopwords')

stop_words=nltk.corpus.stopwords.words('english')
print(len(stop_words))
print(stop_words[:7])
print([sw for sw in stop_words if len(sw)==1])

print(len(sklearn_stop_words))
print(len(stop_words))

st=set(stop_words)
print(type(sklearn_stop_words))
print(type(st))

print(len(st.intersection(sklearn_stop_words)))
print(len(st.union(sklearn_stop_words)))








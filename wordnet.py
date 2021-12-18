from nltk.stem import WordNetLemmatizer
#import ssl
#try:
 #   _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
 #  pass
#else:
 #   ssl._create_default_https_context = _create_unverified_https_context

#nltk.download('wordnet')
from 词干还原 import stemmer

lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("good",pos="a"))
print(lemmatizer.lemmatize("goods",pos="a"))
print(lemmatizer.lemmatize("goods",pos="n"))
print(lemmatizer.lemmatize("goodness",pos="n"))
print(lemmatizer.lemmatize("best",pos="a"))
print(stemmer.stem('goodness'))


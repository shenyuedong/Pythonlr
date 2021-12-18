from nltk.tokenize import TreebankWordTokenizer
from collections import OrderedDict
import copy

tokenizer=TreebankWordTokenizer()

docs=["The faster Harry got to the store, the faster and faster Harry would get home."]
docs.append("Harry is hairy and faster than Jill.")
docs.append("Jill is not as hairy as Harry.")
doc_tokens=[]
for doc in docs:
    doc_tokens+=[sorted(tokenizer.tokenize(doc.lower()))]

print(len(doc_tokens[0]))
all_doc_tokens=sum(doc_tokens,[])
print(len(all_doc_tokens))

lexicon=sorted(set(all_doc_tokens))
print(len(lexicon))
print(lexicon)

zero_vector=OrderedDict((token,0) for token in lexicon)
print(zero_vector)
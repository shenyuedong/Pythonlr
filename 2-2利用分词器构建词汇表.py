import numpy as np
import pandas as pd
sentence="""Thomas Jefferson began building Monticello at the age of 26."""

token_sequence=str.split(sentence)
vocab=sorted(set(token_sequence))
print(vocab)
print(','.join(vocab))

nums_tokens=len(token_sequence)
vocab_size=len(vocab)
print(nums_tokens,vocab_size)
onehot_vectors=np.zeros((nums_tokens,vocab_size),int)

for i,word in enumerate(token_sequence):
    onehot_vectors[i,vocab.index(word)]=1

print(" ".join(vocab))

print(onehot_vectors)

print(pd.DataFrame(onehot_vectors,columns=vocab))

df=pd.DataFrame(onehot_vectors,columns=vocab)
df[df==0]=''
print(df)

sentence_bow={}
for token in sentence.split():
    sentence_bow[token]=1

print(sorted(sentence_bow.items()))

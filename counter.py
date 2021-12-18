from collections import Counter
from itertools import permutations
import numpy as np
print(Counter("Guten Morgen Rosa".split()))
print(Counter("Good morning, Rosa!".split()))

print([" ".join(combo) for combo in
 permutations("Good morning Rosa!".split(),3)])

s="""Find textbooks with titles containing 'NLP', or 'natural' and 'language',or 'computational' and
'linguistics'."""

print(len(set(s.split())))
print(np.arange(1,12+1).prod())

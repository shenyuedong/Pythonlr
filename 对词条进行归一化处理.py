import re
tokens=['House','Visitor','Center']
normalized_tokens=[x.lower() for x in tokens]
print(normalized_tokens)

def stem(phrase):
    return ' '.join([re.findall('^(.*ss|.*?)(s)?$',word)[0][0].strip("'") for word in phrase.lower().split()])

print(stem('houses'))
print(stem("Doctor House's calls"))
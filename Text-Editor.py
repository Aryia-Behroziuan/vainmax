import nltk
import numpy as np
from nltk.tokenize import word_tokenize


URL = str(input('Enter File URL:'))
file = open(URL, encoding="utf-8")
text = file.read()
print(text)

spam = str(input('Enter spam characters with no spaces:'))
bg_spam = list(spam)
for alpha in bg_spam:
    text = text.replace(alpha, "") 
print(text)    
index = open(r'VMax.txt', "a")
index.write(text)

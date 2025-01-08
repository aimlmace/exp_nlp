import re
import nltk
from nltk.text import Text
from nltk.corpus import stopwords

nltk.download('stopwords')

sentences = []
with open('text_concordance.txt','r') as file:
	lines = file.readlines()
	for line in lines:
		punctuation_removed = re.sub(pattern = '[^\w\s]',repl="",string = line)
		sentences.append(punctuation_removed)
stop_words = set(stopwords.words('english'))
tokens = [word for scentence in sentences for word in scentence.split() if word not in stop_words]

text = Text(tokens)

target = input('Enter the word: ')

text.concordance(target)
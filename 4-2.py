import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

sentences = []
with open('text_concordance.txt','r') as file:
	data = file.read()
lines = data.lower().split('.')
for x in lines:
	sentence = punctuation_removed = re.sub(pattern = '[^\w\s]',repl=" ",string = x)
	sentences.append(sentence)
print(len(sentences))

context = int(input('Context: '))
target = input('Word: ')
print()
for scentence in sentences:
	tokens = [lemmatizer.lemmatize(word) for word in scentence.split() if word not in stop_words]
	for i,word in enumerate(tokens):
		if target == word:
			start = max(0, i-context)
			end = min(len(tokens),i+context+1)
			line = ' '.join(tokens[start:end])
			print(line)
			print()
			break



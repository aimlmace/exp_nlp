import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN 

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
	tokens_non = [word for word in scentence.split() if word not in stop_words]
	pos_tags = nltk.pos_tag(tokens_non)
	
	tokens = []
	for word, tag in pos_tags:
	    pos = get_wordnet_pos(tag)
	    lemma = lemmatizer.lemmatize(word, pos=pos)
	    tokens.append(lemma)

	for i,word in enumerate(tokens):
		if target == word:
			start = max(0, i-context)
			end = min(len(tokens),i+context+1)
			line = ' '.join(tokens[start:end])
			print(line)
			print()
			break



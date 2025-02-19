import nltk
import re
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

pos_tags = {
    "CC": "Coordinating conjunction",
    "CD": "Cardinal number",
    "DT": "Determiner",
    "EX": "Existential there",
    "FW": "Foreign word",
    "IN": "Preposition or subordinating conjunction",
    "JJ": "Adjective",
    "JJR": "Adjective, comparative",
    "JJS": "Adjective, superlative",
    "LS": "List item marker",
    "MD": "Modal",
    "NN": "Noun, singular or mass",
    "NNS": "Noun, plural",
    "NNP": "Proper noun, singular",
    "NNPS": "Proper noun, plural",
    "PDT": "Predeterminer",
    "POS": "Possessive ending",
    "PRP": "Personal pronoun",
    "PRP$": "Possessive pronoun",
    "RB": "Adverb",
    "RBR": "Adverb, comparative",
    "RBS": "Adverb, superlative",
    "RP": "Particle",
    "SYM": "Symbol",
    "TO": "To (as part of an infinitive verb)",
    "UH": "Interjection",
    "VB": "Verb, base form",
    "VBD": "Verb, past tense",
    "VBG": "Verb, gerund or present participle",
    "VBN": "Verb, past participle",
    "VBP": "Verb, non-3rd person singular present",
    "VBZ": "Verb, 3rd person singular present",
    "WDT": "Wh-determiner",
    "WP": "Wh-pronoun",
    "WP$": "Possessive wh-pronoun",
    "WRB": "Wh-adverb"
}


def get_file(path):
	sentences = []
	with open(path,'r') as f:
		sentence = f.readlines()
		sentences = [s.strip() for s in sentence]
	return sentences


def get_tag(word):
	if word.startswith('J'):
		return wordnet.ADJ
	elif word.startswith('V'):
		return wordnet.VERB
	elif word.startswith('N'):
		return wordnet.NOUN
	elif word.startswith('R'):
		return wordnet.ADV
	else:
		return wordnet.NOUN

stop_words = set(stopwords.words('english'))

def preprocess(data):
	print(data)
	tokens = data.split()
	tokens = [token for token in tokens if token not in stop_words]
	tag_tokens = nltk.pos_tag(tokens)
	for word,tag in tag_tokens:
		print(word,'\t',tag,'\t', pos_tags[tag])
	l = []
	for word,tag in tag_tokens:
		w = lemmatizer.lemmatize(word,get_tag(tag))
		l.append(w)
	print(l)
	print('\n')
	
	return tag_tokens,l

data = get_file('bow_data.txt')
a= []
l=[]
for d in data:
	k,m = preprocess(d)
	a.extend(k)
	l.append(m)
# for word, tag in a:
# 	print(tag)

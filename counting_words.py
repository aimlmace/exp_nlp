import nltk
import re
from nltk.tokenize import word_tokenize

with open ('data.txt','r') as file:
	data = file.read()

pattern = r'[^\w\s]|https?://\S+|www\.\S+'
punctuation_removed = re.sub(pattern = pattern,repl = '', string = data)

tokens = word_tokenize(punctuation_removed)

print(f'Total Number of Tokens: {len(tokens)}')

set_tokens = set(tokens)

print(f'Total Number of Unique Tokens: {len(set_tokens)}')

for word in set_tokens:
	print(f'{word} occur {tokens.count(word)} times')
	print(f'Percentage: {tokens.count(word)/len(tokens)*100:.2f}')
print()
print(f'TTR: {(len(set_tokens)/len(tokens))*100:.2f}')
print()
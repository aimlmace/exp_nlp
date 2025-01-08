import nltk
import re
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer,PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
print(len(stop_words))
print(stop_words)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
def clean(line):
	print('Line: ',line)

	l_line = line.lower()

	url_pattern = r'https?://\S+|www\.\S+'

	u_line = re.sub(url_pattern,'',l_line)
	
	print('URL Removed: ',u_line)
	

	e_line = emoji.replace_emoji(u_line,replace='')
	print('Emoji Removed: ',e_line)
	

	p_line = re.sub(pattern = '[^\w\s]',repl="",string = e_line)

	print('Punctuation Removed: ',p_line)
	
	
	return p_line

def analyse(line):
	c_line = clean(line)

	stop_words = set(stopwords.words('english'))
	print(len(stop_words))
	words = c_line.split()
	print('Tokenized Words: ',words)
	tokens = [word for word in words if word not in stop_words]
	
	print('Stop Words Removed: ',tokens)


	s_tokens = [stemmer.stem(word) for word in tokens]

	print('Stemmed Words: ',s_tokens)
	

	l_words = [lemmatizer.lemmatize(word) for word in s_tokens]

	print('Lemmatized Words: ',l_words)
	
	cleaned_line = ' '.join(l_words)

	print('Cleaned Line: ',cleaned_line)
	print()
	print()
	
	return cleaned_line




with open('data.txt','r') as file:
	lines = file.readlines()

	cleaned_line = [analyse(line) for line in lines]
	
	with open('cleaned_tweets.txt','w') as f:
		for line in cleaned_line:
			
			f.write(line+ '\n')
		


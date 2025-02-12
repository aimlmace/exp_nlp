import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# nltk.download('stopwods')
# nltk.download('punkt')
# nltk.download('wordnet')

sentences = []

with open('data5.txt', 'r') as file:
	sentence = file.readlines()
	sentences.extend(s.strip() for s in sentence)
	
def preprocess(s):
	
	tokens = word_tokenize(s.lower())
	stop_words = set(stopwords.words('english'))

	tokens = [token for token in tokens if token not in stop_words]

	lemmatizer = WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]

	print(tokens)

	return ' '.join(tokens)

def find(u_input, sentences):
    pre_user_input = preprocess(u_input.strip())
    pre_sentences = [preprocess(s.strip()) for s in sentences]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([pre_user_input] + pre_sentences)
    
    cosine_similarities = (tfidf_matrix * tfidf_matrix.T).toarray()[0][1:]
    similar_index = cosine_similarities.argmax()
    return sentences[similar_index]


u_input = input('Enter input')
# 'hello I am a women' 

print(find(u_input,sentences))
# ans = [preprocess(s) for s in sentences]
# print(ans)

# def find(u_input, scentence):

# 	pre_user_input = preprocess(u_input.strip())

# 	pre_sentences = [preprocess(s.strip()) for s in sentences]

# 	vectorizer = TfidfVectorizer()
	
# 	tfidf_matrix = vectorizer.fit_transform([pre_user_input]+pre_sentences)

# 	print(tfidf_matrix)

# 	score = (tfidf_matrix * tfidf_matrix.T)[0][1:]

# 	similar_index = score.argmax()

# 	scentence = sentences[similar_index]

# 	similarities = tfidf_matrix
# 	# .transform([pre_user_input]+pre_sentences)
# 	print([pre_user_input]+pre_sentences)
# 	score = np.array(similarities.sum(axis=1))[0]

# 	sorted_indices = np.argsort(score)[::-1]
# 	return pre_sentences[sorted_indices[0]]


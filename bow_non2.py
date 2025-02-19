from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize

corpus =  "Python is amazing and fun. Python is not just fun but also powerful. Learning Python is fun!"
corpus = sent_tokenize(corpus)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print("Vocabulary:", vectorizer.get_feature_names_out())

doc1 = "Python is fun."
y = vectorizer.transform([doc1])
print(y.toarray())
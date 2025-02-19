from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import sent_tokenize

corpus = "Python is amazing and fun. Python is not just fun but also powerful. Learning Python is fun!"
corpus = sent_tokenize(corpus)
print("sentences:")
for sent in corpus:
    print(sent)

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(corpus)

print("Vocabulary:", vectorizer.get_feature_names_out())

for idx, sentence in enumerate(corpus):
    sentence_vector = X[idx].toarray()
    print(f"Bag of Words for sentence {idx+1}: {sentence_vector}")
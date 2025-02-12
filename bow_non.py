with open('bow_data.txt','r') as data:
	documents = [line.strip() for line in data.readlines()]
print(documents)
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(binary = True)
X = vectorizer.fit_transform(documents)
print(X)

with open('bow_output.txt', 'w') as f:
    f.write(" ".join(vectorizer.get_feature_names_out()) + "\n")
    for row in X.toarray():
        f.write(" ".join(map(str, row)) + "\n")
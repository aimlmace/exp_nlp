
import nltk 
import re 
import string

text =  "Python is amazing and fun. Python is not just fun but also powerful. Learning Python is fun!"
    	
text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))
tokens = text.split()

vocab = set(tokens)
print(vocab)

def vectorize(doc, vocab):
	vector = {word:0 for word in vocab}
	
	doc = doc.lower()
	doc = doc.translate(str.maketrans("", "", string.punctuation))
	tokens = doc.split()
	
	for word in tokens:
		vector[word] += 1
		
	return list(vector.values())
	
def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    mag_a = (sum(x**2 for x in vector_a)) ** 0.5
    mag_b = (sum(y**2 for y in vector_b)) ** 0.5
    if mag_a == 0 or mag_b == 0:
        return 0
    return dot_product / (mag_a * mag_b)

doc1 = "Python is fun."
v1 = vectorize(doc1,vocab)
print(f"vector of {doc1} : {v1}")
    
doc2 = "python"
v2 = vectorize(doc2,vocab)
print(f"vector of {doc2} : {v2}")

cosine_score = cosine_similarity(v1, v2)
print(f"Cosine Similarity Score: {cosine_score:.4f}")
	
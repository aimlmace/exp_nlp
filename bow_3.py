import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import math

lemmatizer = WordNetLemmatizer()

#for tagging
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

# Preprocess
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text) 
    
    tokens = text.split()  
  
    lemmatized_tokens = []
    for word in tokens:
        lemmatized_tokens.append(lemmatizer.lemmatize(word))
    
    return lemmatized_tokens


documents = []
with open('bow_data.txt', 'r') as data:
    documents = [line.strip() for line in data.readlines()]

doc_vectors = [preprocess_text(doc) for doc in documents]

vocabulary = set()
for doc in doc_vectors:
    vocabulary.update(doc)

vocabulary = list(vocabulary)

vectors = []
for doc in doc_vectors:
    vector = [1 if word in doc else 0 for word in vocabulary]
    vectors.append(vector)

inp = input('Enter Sentence: ')
svector = [1 if word in preprocess_text(inp) else 0 for word in vocabulary]
print(f"Vector for the input sentence: {svector}")

def cosine_similarity(vec1, vec2):
    
    dot_product = sum(x * y for x, y in zip(vec1, vec2))
    
    
    magnitude_vec1 = math.sqrt(sum(x**2 for x in vec1))
    magnitude_vec2 = math.sqrt(sum(y**2 for y in vec2))
    
    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0
    return dot_product / (magnitude_vec1 * magnitude_vec2)

similarities = []
for vector in vectors:
    similarity = cosine_similarity(svector, vector)
    similarities.append(similarity)

for i, sim in enumerate(similarities):
    print(f"Cosine Similarity with Document {i + 1}: {sim:.4f}")

with open('bow_out.txt', 'w') as out:
    for vector in vectors:
        out.write(' '.join(map(str, vector)) + '\n'+ '\n')

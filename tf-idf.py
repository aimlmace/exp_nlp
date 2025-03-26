# Write a python program to find TF-IDF values of each words in a sentence
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample sentences (documents)
corpus = [
    "The cat sat on the mat",
    "The dog sat on the mat",
    "The cat and the dog are friends"
]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the corpus
tfidf_matrix = vectorizer.fit_transform(corpus)

# Get feature names (unique words)
feature_names = vectorizer.get_feature_names_out()



# Convert to DataFrame for better readability
df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# Display the TF-IDF values
print("\nTF-IDF Matrix:\n")
print(df)
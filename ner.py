import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

text = "Barack Obama was born on August 4, 1961, in Honolulu, Hawaii. Apple Inc. is based in Cupertino."

words = word_tokenize(text)
pos_tags = pos_tag(words)
ner_tree = ne_chunk(pos_tags)

print("Named Entities:")
for subtree in ner_tree:
    if isinstance(subtree, nltk.Tree):  # Check if it's a named entity
        entity = " ".join(word for word, tag in subtree.leaves())
        entity_type = subtree.label()  # The type of the entity (e.g., PERSON, GPE)
        print(f"Entity: {entity}, Type: {entity_type}")



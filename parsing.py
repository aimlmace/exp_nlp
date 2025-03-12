# import nltk

# nltk.download('treebank')
# nltk.download('universal_tagset')

# def const_parsing(text):
# text = "the big brown dog barked loudly"
# dep = dep_parse(text)
# for node in dep:
# 	print(node)

# import spacy
# from spacy import displacy

# # Load the pre-trained model
# nlp = spacy.load("en_core_web_sm")

# # Parse a sentence
# sentence = "The cat sat on the mat."
# doc = nlp(sentence)

# # Visualize the syntactic parse tree
# displacy.serve(doc, style="dep")

# import nltk
# from nltk import CFG

# # Define a simple context-free grammar (CFG)
# cfg_grammar = CFG.fromstring("""
#   S -> NP VP
#   NP -> Det N
#   VP -> V NP | V PP
#   PP -> Prep NP
#   Det -> 'the' | 'a'
#   N -> 'dog' | 'cat' | 'mat'
#   V -> 'sat' | 'barked'
#   Prep -> 'on' | 'under'
# """)

# # Define a simple probabilistic context-free grammar (PCFG)
# pcfg_grammar = CFG.fromstring("""
#   S -> NP VP [1.0]
#   NP -> Det N [0.5] | N [0.5]
#   VP -> V NP [0.6] | V PP [0.4]
#   PP -> Prep NP [1.0]
#   Det -> 'the' [0.7] | 'a' [0.3]
#   N -> 'dog' [0.4] | 'cat' [0.3] | 'mat' [0.3]
#   V -> 'sat' [0.6] | 'barked' [0.4]
#   Prep -> 'on' [0.5] | 'under' [0.5]
# """)

# # Create parsers for both CFG and PCFG
# cfg_parser = nltk.ChartParser(cfg_grammar)
# pcfg_parser = nltk.ChartParser(pcfg_grammar)

# # Sentence to parse (as a list of words)
# sentence = ['the', 'dog', 'sat', 'on', 'the', 'mat']

# # Parse the sentence using the regular CFG and display the parse trees
# print("CFG Parse Trees:")
# for tree in cfg_parser.parse(sentence):
#     tree.pretty_print()

# # Parse the sentence using the probabilistic PCFG and display the parse trees
# print("\nPCFG Parse Trees:")
# for tree in pcfg_parser.parse(sentence):
#     tree.pretty_print()

# import spacy
# from nltk import Tree

# # Load the SpaCy English model
# en_nlp = spacy.load("en_core_web_sm")

# # Process the sentence with SpaCy
# doc = en_nlp("The quick brown fox jumps over the lazy dog.")

# def to_nltk_tree(node):
#     """
#     Convert a SpaCy token tree to an NLTK tree
#     """
#     if node.n_lefts + node.n_rights > 0:
#         return Tree(node.dep_, [to_nltk_tree(child) for child in node.children])
#     else:
#         return node.text

# # Convert the root of the sentence to an NLTK tree and pretty print it
# for sent in doc.sents:
#     tree = to_nltk_tree(sent.root)
#     tree.pretty_print()

import spacy
from spacy import displacy

# Load the language model
en_nlp = spacy.load("en_core_web_sm")

# Process the sentence
doc = en_nlp("The quick brown fox jumps over the lazy dog.")

# Render the dependency tree visually in the browser or Jupyter notebook
displacy.render(doc, style="dep", jupyter=True)

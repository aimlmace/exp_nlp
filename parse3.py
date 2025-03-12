import nltk
from nltk import CFG, PCFG, ChartParser
from nltk.tokenize import word_tokenize

nltk.download('punkt')

constituency_grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N | NP PP
  VP -> V NP | VP PP
  PP -> P NP
  Det -> 'the' | 'a'
  N -> 'cat' | 'dog' | 'telescope' | 'man'
  V -> 'saw' | 'ate'
  P -> 'with' | 'on'
""")

probabilistic_grammar = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det N [0.3] | Det N PP [0.4] | 'I' [0.3]
  VP -> V NP [0.4] | V NP PP [0.3] | V PP [0.3]
  PP -> P NP [1.0]
  Det -> 'the' [0.5] | 'a' [0.5]
  N -> 'cat' [0.3] | 'dog' [0.3] | 'telescope' [0.2] | 'man' [0.2]
  V -> 'saw' [0.5] | 'ate' [0.5]
  P -> 'with' [0.5] | 'on' [0.5]
""")

constituency_parser = ChartParser(constituency_grammar)

probabilistic_parser = ChartParser(probabilistic_grammar)

def parse_sentence(sentence):
    tokens = word_tokenize(sentence)
    
 
    print("\nConstituency Parsing (CFG):")
    for tree in constituency_parser.parse(tokens):
        tree.pretty_print() 
        # tree.draw() 

    print("\nProbabilistic Parsing (PCFG):")
    for tree in probabilistic_parser.parse(tokens):
        tree.pretty_print()  

input_sentence = input("Enter a sentence to parse: ").lower()
# The cat saw the dog with a telescope
parse_sentence(input_sentence)

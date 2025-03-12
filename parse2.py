import nltk
from nltk import CFG, PCFG

# Define an expanded context-free grammar (CFG)
cfg_grammar = CFG.fromstring("""
  S -> NP VP | S Conj S
  NP -> Det N | Det Adj N | N | NP PP
  VP -> V NP | V PP | V AdvP | V NP PP | V AdvP PP  # Added "V AdvP PP"
  PP -> Prep NP
  AdvP -> Adv | Adv AdvP
  Det -> 'the' | 'a' | 'some' | 'my'
  N -> 'dog' | 'cat' | 'mat' | 'park' | 'ball' | 'man' | 'woman'
  V -> 'sat' | 'barked' | 'ran' | 'chased' | 'saw' | 'ate'
  Prep -> 'on' | 'under' | 'in' | 'near' | 'by'
  Adj -> 'big' | 'small' | 'red' | 'happy' | 'lazy'
  Adv -> 'quickly' | 'loudly' | 'silently' | 'happily'
  Conj -> 'and' | 'or'
""")

# Define an expanded probabilistic context-free grammar (PCFG)
pcfg_grammar = PCFG.fromstring("""
  S -> NP VP [0.4] | S Conj S [0.6]
  NP -> Det N [0.3] | Det Adj N [0.2] | N [0.2] | NP PP [0.3]
  VP -> V NP [0.3] | V PP [0.25] | V AdvP [0.2] | V NP PP [0.15] | V AdvP PP [0.1]  # Added "V AdvP PP"
  PP -> Prep NP [1.0]
  AdvP -> Adv [1.0]
  Det -> 'the' [0.4] | 'a' [0.3] | 'some' [0.2] | 'my' [0.1]
  N -> 'dog' [0.142857] | 'cat' [0.142857] | 'mat' [0.142857] | 'park' [0.142857] | 'ball' [0.142857] | 'man' [0.142857] | 'woman' [0.142857]
  V -> 'sat' [0.2] | 'barked' [0.2] | 'ran' [0.2] | 'chased' [0.1] | 'saw' [0.1] | 'ate' [0.2]
  Prep -> 'on' [0.3] | 'under' [0.2] | 'in' [0.2] | 'near' [0.2] | 'by' [0.1]
  Adj -> 'big' [0.25] | 'small' [0.25] | 'red' [0.25] | 'happy' [0.125] | 'lazy' [0.125]
  Adv -> 'quickly' [0.3] | 'loudly' [0.3] | 'silently' [0.2] | 'happily' [0.2]
  Conj -> 'and' [0.5] | 'or' [0.5]
""")

# Create parsers for both CFG and PCFG
cfg_parser = nltk.ChartParser(cfg_grammar)
pcfg_parser = nltk.ChartParser(pcfg_grammar)

# Sentence to parse (as a list of words)
sentence = ['the', 'big', 'dog', 'ran', 'quickly', 'on', 'the', 'mat']

# Parse the sentence using the regular CFG and display the parse trees
print("CFG Parse Trees:")
for tree in cfg_parser.parse(sentence):
    tree.pretty_print()

# Parse the sentence using the probabilistic PCFG and display the parse trees
print("\nPCFG Parse Trees:")
for tree in pcfg_parser.parse(sentence):
    tree.pretty_print()


cfg_trees = list(cfg_parser.parse(sentence))
print("CFG Parse Trees:")
if cfg_trees:
    for tree in cfg_trees:
        tree.pretty_print()
else:
    print("No CFG parse trees found.")

# For PCFG
pcfg_trees = list(pcfg_parser.parse(sentence))
print("\nPCFG Parse Trees:")
if pcfg_trees:
    for tree in pcfg_trees:
        tree.pretty_print()
else:
    print("No PCFG parse trees found.")
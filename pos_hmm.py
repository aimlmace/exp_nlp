import nltk
from nltk.tag import hmm
from nltk.corpus import treebank
from nltk.tokenize import word_tokenize

nltk.download('treebank')
nltk.download('punkt')

data = treebank.tagged_sents()[:3000]  

model = hmm.HiddenMarkovModelTrainer()
hmm_tagger = model.train(data)

k = input('Enter scentence: ')

tokens = word_tokenize(k)

tagged = hmm_tagger.tag(tokens)
print(tagged)
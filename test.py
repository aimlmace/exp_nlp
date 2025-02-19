import nltk
from nltk.corpus import treebank
from nltk.tag import hmm
from nltk.probability import FreqDist, ConditionalFreqDist

# Download necessary NLTK datasets if you haven't already
nltk.download('treebank')
nltk.download('punkt')

# Step 1: Load the Treebank corpus and split into training and test sets (90%-10%)
train_sents = treebank.tagged_sents()[:3000]  # Training data
test_sents = treebank.tagged_sents()[3000:]   # Test data

# Step 2: Calculate transition and emission frequencies

# Transition frequencies (tag -> tag) - bigrams of tags
train_tags = [tag for sent in train_sents for word, tag in sent]
tag_bigrams = list(nltk.bigrams(train_tags))
transition_freq = FreqDist(tag_bigrams)

# Emission frequencies (tag -> word) - bigrams of words and tags
word_tag_pairs = [(word, tag) for sent in train_sents for word, tag in sent]
emission_freq = ConditionalFreqDist((tag, word) for word, tag in word_tag_pairs)

# Step 3: Train the HMM POS tagger using NLTK's HiddenMarkovModelTrainer
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_sents)

# Step 4: Test the model on the test set and evaluate its performance
accuracy = hmm_tagger.evaluate(test_sents)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Step 5: Use the trained HMM POS tagger to tag new sentences
sentence = "This is a new sentence".split()  # Example sentence
tagged_sentence = hmm_tagger.tag(sentence)  # POS tagging
print("Tagged Sentence:", tagged_sentence)

# Optional: Using pre-trained POS tagger in NLTK (alternative approach)
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Tokenize and tag a new sentence using pre-trained tagger
tokens = word_tokenize("This is a simple sentence")
pretrained_tags = pos_tag(tokens)
print("Pre-trained POS Tags:", pretrained_tags)

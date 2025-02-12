documents = []

#reading each line from the file
with open('bow_data.txt','r') as data:
	documents = [line.strip() for line in data.readlines()]

#doc_vectors store every tockens from all scentences
doc_vectors = [doc.split() for doc in documents]

#vocabulary is used to get the unique tokens.

vocabulary = set()
for doc in doc_vectors:
	vocabulary.update(doc)

#every word from the corpus is added to the set and the this set vocabulary is converted to list for indexing
vocabulary = list(vocabulary)

print(doc_vectors)
print()
print(vocabulary)
print()


vectors = []
#each line from the file is taken
for doc in doc_vectors:
	vector = []
	'''
	comparing each word in the vocabulary
	if the word in the vocabulary is present 1 is added to vector else 0
	'''
	for word in vocabulary:
		if word in doc:
			vector.append(1)
		else:
			vector.append(0)
	vectors.append(vector)	
	print(vector)
#read a user input and print the vector
inp = input('Enter Scentence').split()
for word in vocabulary:
	if word in inp:
		svector.append(1)
	else:
		svector.append(0)
print(svector)

with open('bow_out.txt','w')as out:
	for line in vectors:
		out.write(' '.join(map(str, vector)) + '\n')

	
import re
sentences = []
with open('text_concordance.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        punctuation_removed = re.sub(pattern = '[^\w\s]',repl="",string = line)
        sentences.append(punctuation_removed)


stop_words = set(['further', 'o', "mustn't", 'into', 'most', 'nor', 'themselves', "you're", 'with', 'in', 'as', 'be', 'can', 'isn',
 "aren't", 'was', 'down', 'having', 'this', 'to', 'theirs', 'ma', "you'll", 'has', 'because', 'doing', 'do', 'it', 
 'why', 'if', 'than', 'each', 'what', "it's", 'her', "isn't", 'all', 'on', 've', 'they', 'is', 'doesn', 'once', 'hasn', 
 'should', 'y', 'during', "hasn't", "weren't", 'over', 'weren', 'she', 'but', 'too', 'couldn', "wouldn't", 'am', 'myself', 
 'where', "you've", 'above', 'against', 'had', 'until', 'below', "that'll", 'and', 'not', 'them', "haven't", 'through', 
 "needn't", "you'd", "shouldn't", 'or', 'those', 'your', 'same', 'll', "mightn't", 'ourselves', "didn't", 're', 'such', 
 'up', 'when', 'd', 'so', 'under', 'between', 'were', 'own', 'at', 'here', 'yours', "wasn't", 'did', "should've", 'again',
  'my', 'few', 'he', 'wasn', 'only', "shan't", 'does', 'didn', 'you', 'any', "doesn't", 'an', 'for', 'after', 'before', 'more',
   'needn', 'then', 'hers', 'ours', 'out', 'himself', 'of', 'who', 'both', 'will', 'being', 'from', 'our', 'off', 'whom', 't', 
   'about', 'him', 'haven', 'the', "hadn't", 'herself', 'won', 'now', "she's", 'been', 'aren', 'hadn', 'mustn', 'which', 'i', 'its', 
   'yourselves', 'a', "won't", 'm', 'just', 'some', 'that', 'itself', 'mightn', 'other', 'while', 'by', 'these', 'how', 'there', "don't", 
   'ain', 'we', 's', 'wouldn', 'their', 'very', 'shan', 'yourself', 'me', 'his', 'have', 'don', "couldn't", 'are', 'shouldn', 'no'])


tokens = [word for scentence in sentences for word in scentence.split() if word not in stop_words]

target = input('Enter Word: ')

window = 5

for i,word in enumerate(tokens):

    if word.lower() == target.lower():
        start = max(0, i-window)
        end = min(len(tokens),i+window+1)
        context = ' '.join(tokens[start:end])

        print(context)
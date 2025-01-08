# stop_words = set([
#     'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 
#     'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 
#     'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
#     'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 
#     'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
#     'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 
#     'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
#     'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 
#     'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
#     'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 
#     'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', 
#     "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 
#     'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 
#     'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
# ])

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


def stemmer(word):
    if word.endswith('ing'):
        return word[:-3]
    elif word.endswith('ly'):
        return word[:-2]
    elif word.endswith('ed'):
        return word[:-2]
    elif word.endswith('es'):
        return word[:-2]
    elif word.endswith('s'):
        return word[:-1]
    return word


def lemmatizer(word):
    irregulars = {
        'is': 'be', 'am': 'be', 'are': 'be', 'was': 'be', 'were': 'be',
        'has': 'have', 'have': 'have', 'had': 'have',
        'go': 'go', 'goes': 'go', 'going': 'go', 'went': 'go', 'gone': 'go'
    }
    return irregulars.get(word, word)

ef clean(line):
    print('Line: ', line)


    l_line = line.lower()
   
    url_pattern = r'https?://\S+|www\.\S+'
    u_line = re.sub(url_pattern, '', l_line)
    print('URL Removed: ', u_line)
 
    e_line = u_line.encode('ascii', 'ignore').decode('ascii')
    print('Emoji Removed: ', e_line)
    
    p_line = re.sub(r'[^\w\s]', '', e_line)
    print('Punctuation Removed: ', p_line)
    
    return p_line

def analyse(line):
    c_line = clean(line)


    words = c_line.split()
    print('Tokenized Words: ', words)
    

    tokens = [word for word in words if word not in stop_words]
    print('Stop Words Removed: ', tokens)

    s_tokens = [stemmer(word) for word in tokens]
    print('Stemmed Words: ', s_tokens)
 
    l_words = [lemmatizer(word) for word in s_tokens]
    print('Lemmatized Words: ', l_words)

    cleaned_line = ' '.join(l_words)
    print('Cleaned Line: ', cleaned_line)
    print()
    print()
    
    return cleaned_line

with open('data.txt', 'r') as file:
    lines = file.readlines()

    cleaned_lines = [analyse(line) for line in lines]

    with open('cleaned_tweets.txt', 'w') as f:
        for line in cleaned_lines:
            f.write(line + '\n')
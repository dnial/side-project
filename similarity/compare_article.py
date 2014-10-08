from nltk.corpus import stopwords
import re, similarity_index, sys
from collections import Counter

def get_file_content(filepath):
    f = open(filepath, "r")
    article = ""
    try:
        # Read the entire contents of a file at once.
        article = f.read()
    finally:
        f.close()
    
    return article
    
def get_important_words(article, stopwords):
    words = re.findall(r'\w+', article) 
    
    important_words = filter(lambda x: x.lower() not in stopwords, words)
    
    return important_words 

def get_stop_words():
    filepath = "english_stopword.txt"
    stopword_list = ()
    for line in open(filepath, 'r'):
        stopword_list += (line.strip(), )

    return stopword_list
    

if sys.argv<>None:
    if (len(sys.argv)<=1):
        sys.exit()
    else:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
    
article_1 =  get_file_content(filename1)
article_2 =  get_file_content(filename2)

stopwords = get_stop_words()

words_1 = get_important_words(article_1, stopwords)
words_2 = get_important_words(article_2, stopwords)

#print words_1
#print words_2
word_vector_1 = Counter(words_1)
word_vector_2 = Counter(words_2)

word_set_1 = set(words_1)
word_set_2 = set(words_2)

cosine = similarity_index.get_cosine(word_vector_1, word_vector_2)
jaccard = similarity_index.get_jaccard_index(word_set_1, word_set_2)
sorensen = similarity_index.get_sorensen_index(word_set_1, word_set_2)
morisita = similarity_index.get_morisita_index(word_vector_1, word_vector_2)

print "Article: %s and article: %s - Result:" % (filename1, filename2)
print "cosine: %s" % cosine
print "jaccard: %s" % jaccard
print "sorensen: %s" % sorensen
print "morisita: %s" % morisita


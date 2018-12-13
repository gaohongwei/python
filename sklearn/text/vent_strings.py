# Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
 ]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
# ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
print(X.toarray())  
# [[0 1 1 1 0 0 1 0 1]
#  [0 2 0 1 0 1 1 0 1]
#  [1 0 0 1 1 0 1 1 1]
#  [0 1 1 1 0 0 1 0 1]]

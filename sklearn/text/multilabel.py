import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

X_train = np.array(["new york is a hell of a town",
                "new york was originally dutch",
                "the big apple is great",
                "new york is also called the big apple",
                "nyc is nice",
                "people abbreviate new york city as nyc",
                "the capital of great britain is london",
                "london is in the uk",
                "london is in england",
                "london is in great britain",
                "it rains a lot in london",
                "london hosts the british museum",
                "new york is great and so is london",
                "i like london better than new york"])
y_train_text = [["new york"],["new york"],["new york"],["new york"],    
                ["new york"],["new york"],["london"],["london"],         
                ["london"],["london"],["london"],["london"],
                ["new york","England"],["new york","london"]]

X_test = np.array(['nice day in nyc',
               'welcome to london',
               'london is rainy',
               'it is raining in britian',
               'it is raining in britian and the big apple',
               'it is raining in britian and nyc',
               'hello welcome to new york. enjoy it here and london too'])

y_test_text = [["new york"],["new york"],["new york"],["new york"],["new york"],["new york"],["new york"]]


lb = preprocessing.MultiLabelBinarizer(classes=("new york","london","England"))
Y = lb.fit_transform(y_train_text)
Y_test = lb.fit_transform(y_test_text)

print Y_test

classifier = Pipeline([
('vectorizer', CountVectorizer()),
('tfidf', TfidfTransformer()),
('clf', OneVsRestClassifier(LinearSVC()))])

classifier.fit(X_train, Y)
predicted = classifier.predict(X_test)
print(predicted)

print("Accuracy Score: ")
print(accuracy_score(Y_test, predicted))

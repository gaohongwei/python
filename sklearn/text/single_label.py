#!/usr/bin/python3
import sys
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics

import pandas as pd

import pprint
from sklearn.model_selection import train_test_split

def start_learn():
  pp = pprint.PrettyPrinter(indent=2)
  #
  #
  # # comma delimited is the default
  csv_file = sys.argv[1]
  df = pd.read_csv(csv_file, names=['txt', 'target'])

  X = df ['txt']
  y = df['target']

  X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75)
  y_true = y_test


  classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))
  ]) # 0.5

  classifier.fit(X_train, y_train)
  y_pred = classifier.predict(X_test)
  precision_score = metrics.precision_score(y_test, y_pred, average='macro')

  metrics.recall_score(y_test, y_pred, average='micro')

  metrics.f1_score(y_test, y_pred, average='weighted')

  metrics.fbeta_score(y_test, y_pred, average='macro', beta=0.5)

  #
  # from collections import Counter
  # Counter(df["target"])
  pct = precision_score*100
  msg = "Correctness Percentage is %s" % pct
  print(msg)
  return precision_score
start_learn()

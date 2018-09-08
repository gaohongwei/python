def eval_model(Xtest,Ytest,train_model):
  # Predicting the Test set results
  Ypred = train_model.predict(Xtest)
  # Performance Evaluation
  from sklearn.metrics import confusion_matrix
  from sklearn.metrics import accuracy_score
  cm = confusion_matrix(Ytest, Ypred)
  print(cm)
  print(accuracy_score(Ytest, Ypred))

def select_training_model():
  #from sklearn.ensemble import RandomForestClassifier
  #classifier = RandomForestClassifier(max_depth=2, random_state=0)
  from sklearn import linear_model
  model = linear_model.LogisticRegression(C=1e5)
  return model

def pca_processing(X_train, X_test):
  from sklearn.preprocessing import StandardScaler
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)
  from sklearn.decomposition import PCA
  pca = PCA()
  pca.fit(X_train)
  Xtrain = pca.transform(X_train)
  Xtest = pca.transform(X_test)
  return [Xtrain, Xtest]

import numpy as np
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv(url, names=names)
dataset.head()
X = dataset.drop('Class', 1)
y = dataset['Class']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Do the real work
Xtrain, Xtest = pca_processing(X_train, X_test)
model = select_training_model()
model.fit(Xtrain, y_train)
eval_model(Xtest,y_test,model)

def select_training_model():
  #from sklearn.ensemble import RandomForestClassifier
  #classifier = RandomForestClassifier(max_depth=2, random_state=0)
  from sklearn import linear_model
  params = {'C': 1e5}
  model = linear_model.LogisticRegression(**params)  
  #       linear_model.LogisticRegression(C=1e5)
  return model

def eval_model(Xtest,Ytest,train_model):
  # Predicting the Test set results
  Ypred = train_model.predict(Xtest)
  # Performance Evaluation
  from sklearn.metrics import confusion_matrix
  from sklearn.metrics import accuracy_score
  cm = confusion_matrix(Ytest, Ypred)
  print(cm)
  print(accuracy_score(Ytest, Ypred))

def select_pca(pct_sum):
  comp_len = len(pct_sum)
  index = 0
  last_sum = 0.0
  while index < comp_len:
    current_sum = pct_sum[index]
    current_pct = current_sum - last_sum
    last_sum = current_sum
    if ( current_sum > 0.95 and current_pct < 0.01 ) or \
       ( current_sum > 0.90 and current_pct < 0.02):
      break
    else:
      index += 1
  return index


def pca_transfrom(X_train, X_test):
  # Normalize the data
  from sklearn.preprocessing import StandardScaler
  sc = StandardScaler()
  Xtrain = sc.fit_transform(X_train)
  Xtest = sc.transform(X_test)
  # Do PCA
  from sklearn.decomposition import PCA
  pca = PCA()
  pca.fit(X_train)
  # Recreate PCA with selected components
  pca_count = select_pca(pca.explained_variance_ratio_.cumsum())
  pca = PCA(n_components=pca_count)
  pca.fit(Xtrain)
  print(pca.explained_variance_ratio_)
  print(pca_count)
  # Transform data
  Xtrain = pca.transform(X_train)
  Xtest = pca.transform(X_test)
  return [Xtrain, Xtest]

# Main code
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
Xtrain, Xtest = pca_transfrom(X_train, X_test)
model = select_training_model()
model.fit(Xtrain, y_train)
eval_model(Xtest,y_test,model)

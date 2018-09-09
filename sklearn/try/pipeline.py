def try_pipeline():
  from sklearn.pipeline import Pipeline
  from sklearn.svm import SVC
  from sklearn.decomposition import PCA
  from sklearn.preprocessing import StandardScaler
  from sklearn.linear_model import LogisticRegression
  from sklearn.datasets import load_digits
  from sklearn.model_selection import train_test_split
  digits = load_digits()
  X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.20, random_state=0)
  pipe = Pipeline([
    ('sc', StandardScaler()),
    ('pca', PCA()),
    ('svc',SVC())
    ])
  pipe.fit(X_train,y_train)
  print(pipe.score(X_test,y_test))

try_pipeline()

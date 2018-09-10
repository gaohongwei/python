def create_pipeline(model, pca_count):
  from sklearn.pipeline import Pipeline
  from sklearn.decomposition import PCA
  from sklearn.preprocessing import StandardScaler
  pipe = Pipeline([
    ('sc', StandardScaler()),
    ('pca', PCA(n_components=pca_count)),
    ('model',model)
    ])
  return pipe

def try_pipeline():
  from sklearn.svm import SVC
  from sklearn.datasets import load_digits
  digits = load_digits()
  from sklearn.model_selection import train_test_split  
  X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.20, random_state=0)
  model = SVC()
  pca_count = find_pca_count(X_train)
  pipe = create_pipeline(model, pca_count)
  pipe.fit(X_train,y_train)
  print(pipe.score(X_test,y_test))

def try_pipeline_cv():
  from sklearn import linear_model
  model = linear_model.LogisticRegression(C=1e5)
  # PCA count
  from sklearn.datasets import load_digits
  digits = load_digits()
  pca_count = find_pca_count(digits.data)
  # Create pipe
  pipe = create_pipeline(model, pca_count)
  # Create CV
  from sklearn.model_selection import cross_val_score
  from sklearn.model_selection import cross_validate
  scores = cross_validate(pipe, digits.data, digits.target,
                          cv=10, return_train_score=True)
  return scores  
  
def try_pipeline0():
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

try_pipeline0()

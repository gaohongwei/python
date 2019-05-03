pipe = Pipeline([('reduce_dim', LinearDiscriminantAnalysis()),('classify', LogisticRegression())])
param_grid = [{'classify__penalty': ['l1', 'l2'],
               'classify__C': [0.05,0.1, 0.3, 0.6, 0.8, 1.0]}] 

gs = GridSearchCV(pipe, param_grid=param_grid, cv=5, scoring='roc_auc', n_jobs=3)
gs.fit(X, y)

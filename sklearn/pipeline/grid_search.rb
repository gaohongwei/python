grid search. 
let the computer automatically discover the optimum hyperparameters for your algorithm.

param_grid = [
    { 'classify__max_depth': [5,10,15,20] }
]

grid_search = GridSearchCV(pipeline, param_grid=param_grid)
grid_search.fit(features, labels)

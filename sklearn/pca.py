Select dimension
  pca.explained_variance_ratio_
  pca.explained_variance_ratio_ parameter returns 
    a vector of the variance from each dimension. 

  pca.explained_variance_ratio_.cumsum() return 
  a vector x of cumulative variance 


  import numpy as np
  from sklearn.decomposition import PCA

  np.random.seed(0)
  my_matrix = np.random.randn(20, 5)

  my_model = PCA(n_components=5)
  my_model.fit_transform(my_matrix)

  my_model.explained_variance_
  my_model.explained_variance_ratio_
  my_model.explained_variance_ratio_.cumsum()

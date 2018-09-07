Select dimension
  pca.explained_variance_ratio_
  pca.explained_variance_ratio_ parameter returns 
    a vector of the variance from each dimension. 

  pca.explained_variance_ratio_.cumsum() return 
  a vector x of cumulative variance 


  import numpy as np
  from sklearn.decomposition import PCA
  import matplotlib
  matplotlib.use('Agg') # agg
  import matplotlib.pyplot as plt # keep order

  np.random.seed(0)
  my_matrix = np.random.randn(20, 6)

  # pca = PCA().fit(my_matrix)
  pca = PCA()
  pca.fit(my_matrix)

  pca.explained_variance_
  pca.explained_variance_ratio_
  pca.explained_variance_ratio_.cumsum()

  plt.plot(np.cumsum(pca.explained_variance_ratio_))
  plt.xlabel('number of components')
  plt.ylabel('cumulative explained variance');

  plt.savefig('myfig')

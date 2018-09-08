PCA is an unsupervised machine learning
  It depends only upon the feature set 
     does not depend the label/target data.
Data preparation
  PCA performs best with a normalized feature set
  Do standard scalar normalization to normalize feature set

PCA explained_variance_ratio_
  pca.explained_variance_ratio_
    A vector of the variance from each dimension. 

  pca.explained_variance_ratio_.cumsum() 
    A vector x of cumulative variance 

Load library
  import numpy as np
  from sklearn.decomposition import PCA
  import matplotlib
  matplotlib.use('Agg') # agg
  import matplotlib.pyplot as plt # keep order

Sample with random data
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




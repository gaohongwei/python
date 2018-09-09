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

def select_pca_by_variance(pct_sum):
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

def find_pca_count(X):
  from sklearn.preprocessing import StandardScaler
  from sklearn.decomposition import PCA  
  sc = StandardScaler()
  Xpca = sc.fit_transform(X)
  pca = PCA()
  pca.fit(Xpca)
  return select_pca_by_variance(pca.explained_variance_ratio_.cumsum())

def try_pca():
  #Load library
  import numpy as np
  from sklearn.decomposition import PCA
  import matplotlib
  matplotlib.use('Agg') # agg
  import matplotlib.pyplot as plt # keep order
  #Sample with random data
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

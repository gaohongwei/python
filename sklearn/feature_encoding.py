
LabelEncoder
  turn [dog,cat,dog,mouse,cat] into [1,2,1,3,2],
  use index
  Problem:  (1+3)/2 =2 
  the imposed ordinality means that the average of dog and mouse is cat.
  Works fine for some algorithms like decision trees and random forests
  LabelEncoder can be used to store values using less disk space.

One-Hot-Encoding has 
  The advantage, 
    the result is binary rather than ordinal 
    everything sits in an orthogonal vector space. 
  The disadvantage 
    high cardinality, 
    the feature space can really blow up quickly

  Solution:
    typically employ one-hot-encoding followed by PCA for dimensionality reduction. 
    The judicious combination of one-hot plus PCA can seldom be beat by other encoding schemes. PCA finds the linear overlap, so will naturally tend to group similar features into the same feature.

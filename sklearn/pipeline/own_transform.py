A pipeline component is defined as a TransformerMixin derived class with three important methods:

fit - Uses the input data to train the transformer
transform - Takes the input features and transforms them

from sklearn.base import TransformerMixin
class MyCustomStep(TransformerMixin):
  def transform(X, **kwargs):
    pass
    
  def fit(X, y=None, **kwargs):
    return self
   
  #if you've build your own transformer components 
  # you need to implement this method to 
  # support the grid search algorithm: 
  def get_params(**kwargs):
    return { }

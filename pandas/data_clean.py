# pip install jupyter
# jupyter notebook
import pandas as pd
import numpy as np
"""
    pd.to_numeric:
        convert string into float
        bad data => np.nan
        np.nan is float
    astype(int):
        data with np.nan

"""
df_number_data = {  
    'number_float': [0.1, 0.2, 0.3, 0.4, 0.5],
    'number_int': [1, 2, 3, 4, 5],        
    'int_has_nan': [1, 2, 3, np.NaN, 5],     
    'float_has_nan': [np.NaN, 0.2, 0.3, 0.4, 0.5],         
}
df = pd.DataFrame(df_number_data)
df['float_has_nan'].astype(int), XXX
df['int_has_nan'].astype(int), XXX

df_str_number_data = {  
    'str_int': ["10","20","40","40","50"],  
    'str_float': ["1.0","2.0","3.0","4.0","5.0"],         
}
df = pd.DataFrame(df_number_data)
df['str_int'].astype(int)
df['str_int'].astype(float)
df['str_float'].astype(float)
df['str_float'].astype(int), xxx
df['str_float'].astype(float).astype(int)


df_string_data = {     
    'int_str_with_str': ["10","20","abc","NaN","50"] ,
    'float_str_with_str': ["abc","NaN","3.0","4.0","5.0"], 
    'number_with_str': [1, 2, 3, 'bad', 5],             
}

df = pd.DataFrame(df_string_data)
df.dtypes

#Failed:
df['int_str_with_str'].astype(float)
df['float_str_with_str'].astype(float)
df['number_with_str'].astype(float)

#Worked: pd.to_numeric, convert to float
pd.to_numeric(df['int_str_with_str'],errors='coerce')
pd.to_numeric(df['float_str_with_str'],errors='coerce')
pd.to_numeric(df['number_with_str'],errors='coerce')

# np.isreal to check the type of each element 
# applymap applies a function to each element 
df.applymap(np.isreal)

# So to get the subDataFrame of rouges, 
# Note: the negation, ~, of the above finds the ones which have at least one rogue non-numeric):
df[~df.applymap(np.isreal).all(1)]

df.applymap(lambda x: isinstance(x, (int, float)))

Update:
cols=['col1', 'col2']
df.loc[2,cols]=[1,2]

Selection:
  loc,  by label index 
    loc[startrow:endrow, startcolumn:endcolumn]
    loc["Alaska":"Arkansas","2005":"2007"]  
  iloc, by integer index, if no row or column labels
    iloc[0:3,0:4]
  ix, avoid to use it, use loc and iloc whenever possible.
    ix[0:3,"2005":"2007"]

Select rows by labels
  df.loc[0,:] # df[1:3] 
  df.loc[0:2,:]
  df.loc[[0,2,3],:]
  On boolean
Select rows by boolean  
  df.loc[df.City == 'Abilene']
Select columns:
  df.loc[:,['City', 'State']]
  df.loc[:,'City':'State']
  df.loc[:,'City']
Select a single cell
  df.loc[1,'City']

Other usage:
  They are short form of above. Avoid to use them

  df[df.City == 'Abilene']  
  df[['City', 'State']]
  df['City']  


Set values by loc 
  # Change the first name of all rows with an ID greater than 2000 to "John"
  data.loc[data['id'] > 2000, "first_name"] = "John"

  # Change the first name of all rows with an ID greater than 2000 to "John"
  data.loc[data['id'] > 2000, "first_name"] = "John"
Assigning an index column
  new_df = df.set_index("State", drop = False)

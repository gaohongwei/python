Loop on rows:
  for index, row in df.iterrows():  
    print(index, row)

  for index, row in df.iteritems():  
    print(index, row)  

Loop on columns:
  for (columnName, columnData) in df.iteritems():
    print('Colunm Name : ', columnName)
    print('Column Contents : ', columnData.values)

  for column in df:
    print('Colunm Name : ', column)

Extracting 
  df.loc[startrow:endrow, startcolumn:endcolumn]

  df.loc["Alaska":"Arkansas","2005":"2007"]

Extracting a column
  df.loc[: , "2005"]
  df["2005"]
  df.loc[:,"2005"].mean()

  Extracting specific columns
  df[["2005", "2008", "2009"]]


Extracting a row
  df.loc["California", : ]


Extracting specific rows
  df[1:3]

Extracting a single cell
  df.loc["California","2013"]

iloc, if no row or column labels
  df.iloc[0:3,0:4]
ix, use loc and iloc whenever possible.
  df.ix[0:3,"2005":"2007"]

Assigning an index column
  new_df = df.set_index("State", drop = False)

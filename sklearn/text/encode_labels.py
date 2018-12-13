# doc
  from sklearn.preprocessing import MultiLabelBinarizer

  multilabel_binarizer = MultiLabelBinarizer()
  multilabel_binarizer.fit(df_questions.Tags)
  y = multilabel_binarizer.classes_
# encode labels
  from sklearn.preprocessing import MultiLabelBinarizer
  mlb = MultiLabelBinarizer()

  labels= [ ['a1', 'a2'], ['a1', 'a3', 'a5'] ]
  Y = mlb.fit_transform(labels)

  list(mlb.classes_)
  print(mlb.classes_)

Loop on a dict
  for key, value in a_dict.items():
    print(key, '->', value)
  In Py2.x
      dict.items(): Return a copy of the dictionary’s list of (key, value) pairs.
      dict.iteritems(): Return an iterator over the dictionary’s (key, value) pairs.
  In Py3.x, 
      dict.items(), dict.keys() and dict.values()
      Returns iterators

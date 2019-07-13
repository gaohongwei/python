#!/usr/bin/python3
def m2(a='aaa', b=2):
  return a*b
if __name__ == '__main__':
  params1 = {
    'a': 10,
    'b': 2
  }
  params2 = {
    'a': 10,
    'b': 20
  }
  params3 = {
    'a': 'abc',
    'b': 3
  }
  print(m2(a=10,b=20))
  print(m2(**params1))
  print(m2(**params2))
  print(m2(**params3))

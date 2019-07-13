#!/usr/bin/python3
def m2(a='aaa', b=2):
  return a*b
if __name__ == '__main__':
  p1 = {
    'a': 10,
    'b': 2
  }
  p2 = {
    'a': 10,
    'b': 20
  }
  p3 = {
    'a': 'abc',
    'b': 3
  }
  p4 = {}
  print(m2(a=10,b=20))
  print(m2(**p1))
  print(m2(**p2))
  print(m2(**p3))
  print(m2(**p4))

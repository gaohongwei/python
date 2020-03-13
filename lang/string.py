# String interpolation
def inject_variable(str_format, values):
  return str_format.format(**values)

def test():
  values = {"name": "Eric", "age": 74}
  str_format = "Hello, {name}. You are {age}."
  return inject_variable(str_format, values)
  
test()

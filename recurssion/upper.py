# First uppercase letter in a string

inps = 'geeksforgeeKs'
output = 'K'

def func(input, n):
  if input == '':
    return 0
  if input[n].isupper():
      return input[n]   
  else:
    return func(input, n+1)

  
print(func(inps, 0))
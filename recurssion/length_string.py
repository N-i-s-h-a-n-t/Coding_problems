# Program for length of a string using recursion

input = 'abcd'
# output: 4

def lenOfString(inp):
  if inp == '':
    return 0
  else:
    return lenOfString(inp[:-1]) + 1 


print(lenOfString('abcde'))
# Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function.

def recursiverange(num):
  if num == 1:
    return 1
  else:
    return num + recursiverange(num-1)

print(recursiverange(10))
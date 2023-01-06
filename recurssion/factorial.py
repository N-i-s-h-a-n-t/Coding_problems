# write a function which accepts a number and returns the factorial
# of that number

def fact(num):
  if num == 1:
    return num
  else:
    return num * fact(num -1)

print(fact(7))
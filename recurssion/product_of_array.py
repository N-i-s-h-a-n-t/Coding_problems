# write a func called productOf array which takes in an array of numbers
# and returns the product of them all

def product(arr):
  if len(arr) == 1:
    return arr[-1]
  else:
    return arr[-1] * product(arr[:-1])

print(product([1, 2, 3, 10]))
# Write a recursive function called someRecursive which accepts an array
#  and a callback. The function returns true if a single value in the array returns true when passed to the callback.
#  Otherwise it returns false.


def isOdd(number):
  if number % 2 == 1:
    return True
  else:
    return False  

def someRecursive(arr, isOdd):
  if len(arr) == 0:
    return False
  else:
    if isOdd(arr[-1]):
      return True
    else:
      return someRecursive(arr[:-1], isOdd) 

print(someRecursive([4,6,8], isOdd))
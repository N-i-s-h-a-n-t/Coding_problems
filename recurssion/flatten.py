# Write a recursive function called flatten
# which accepts an array of arrays and returns a new array with all values flattened.

def flatten(arr):
  resultarr = []
  for i in arr:
    if type(i) is list:
      resultarr.extend(flatten(i))
    else:
      resultarr.append(i)
  return resultarr

print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))
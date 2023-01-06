# Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an object which may contain nested objects.

def nestedEvenSum(obj):
  sum = 0
  for key in obj:
    if type(obj[key]) is int:
      sum += obj[key]
    elif type(obj[key]) is dict:
      sum += nestedEvenSum(obj[key])

  return sum

obj1 = {
  "outer": 2,
  "master":2
  # "obj": {
  #   "inner": 2,
  #   "otherObj": {
  #     "superInner": 2,
  #     "notANumber": True,
  #     "alsoNotANumber": "yup"
  #   }
  # }
}

print(nestedEvenSum(obj1))
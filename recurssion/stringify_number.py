# Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings.

def stringifyNumbers(obj):
  for key in obj:
    if type(obj[key]) is int:
      obj[key] = str(obj[key])
    if type(obj[key]) is dict:
      stringifyNumbers(obj[key])
  return obj



obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))
# Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.

words = ['i', 'am', 'learning', 'recursion']

def capitalizeWords(words):
  result = []
  if len(words) == 0:
    return result
  else:
    result.append(words[0].upper())
    return  result + capitalizeWords(words[1:])


print(capitalizeWords(words))
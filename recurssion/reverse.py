# Write a recursive function called reverse which accepts a string and returns a new string in reverse.

def reverse(word):
  if word == '':
    return ''
  else:
    return str(word[-1])  + reverse(word[:-1])

print(reverse('python'))
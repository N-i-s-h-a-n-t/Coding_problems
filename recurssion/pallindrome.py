# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome

def isPallindrome(word):
  if word == '':
      return ''
  else:
    new_word = word[-1] + isPallindrome(word[:-1])
    return new_word

def check(word):
  if isPallindrome(word) == word:
    return True
  else:
    return False

print(check('amanaplanacanalpanama'))  

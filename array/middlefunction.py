# write a function called middle that takes a list
# returns a new list that contains all but the first and last elements

mylist = [1, 2, 3, 4]

def middle(arr):
  arr = arr[1:-1]
  return arr

print(middle(mylist))
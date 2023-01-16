# is unique: implement an algorithm to determine if a list has all unique characters
# using python list

mylist = [1, 20, 20, 30, 44, 5, 56 ,57 ,8 ,7 , 3, 34 ,12, 23, 13, 14]

def isUnique(mylist):
  visited = []
  for i in mylist:
    if i in visited:
      return "Python list is not unique"
    else:
      visited.append(i)
  return "Python list is unique"

print(isUnique(mylist))
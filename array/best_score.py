# given a list write a function to get first, second
# best scores from the list

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def best_score(list1):
  prev = 0
  max = 0
  for i in range(len(list1)):
    if list1[i] > max:
      prev = max
      max = list1[i]

  return max, prev

print(best_score(myList))
# Given 2d list calculate the sum of diagonal elements

myList2D= [[0,2,3],[4,5,6],[7,4,9]]

def sumOfDiagonal(arr):
  sum = 0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if i == j:
        sum += arr[i][j]

  return sum


print(sumOfDiagonal(myList2D))


# given an image represented by an N x N matrix write a method to rotate the image by 90 degrees.list
# 
# 1   2   3               7   4   1      
# 4   5   6    ------->   8   5   2
# 7   8   9               9   6   3


list1 = [[1,2,3],[4,5,6],[7,8,9]]
# print(list1[0][0])

def rotate(array):
  n = len(array) # row
  for layer in range(n//2):
    first = layer
    last = n - layer - 1
    for i in range(first, last):
      # save top element
      top = array[layer][i]
      # move element to top
      array[layer][i] = array[-i-1][layer]
      #move bottom to left
      array[-i-1][layer] = array[-layer-1][-i-1]
      # move right to bottom
      array[-layer-1][-i-1] = array[i][-layer-1]
      #  move to the right
      array[i][-layer-1] = top

  return array

print(rotate(list1))

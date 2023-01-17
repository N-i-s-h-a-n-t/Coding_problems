# python program to add two matrix

mat1 = [[1,2,3],[4,5,6],[7,8,9]]

mat2 = [[9,8,7],[6,5,4],[3,2,1]]

def addToMatrix(a, b):
  if len(a) != len(b) and len(a[0]) != len(b[0]):
    print("Matrix are not equal")
    return
  else:
    for i in range(len(a)):
      for j in range(len(a[0])):
        print(a[i][j] + b[i][j], end=' ')
      print()

addToMatrix(mat1, mat2)


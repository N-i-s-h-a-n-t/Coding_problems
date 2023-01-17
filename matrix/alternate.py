# print a matrix in alternate manner 
# (left to right then right to left)

#   1   2   3         1   2   3
#   4   5   6         6   5   4
#   7   8   9         7   8   9

mat  = [[1,2,3],[4,5,6],[7,8,9]]

def alternate(a):
  k = len(a[0]) - 1
  for i in range(len(a)):
    for j in range(len(a[0])):
      if i % 2 == 0:
        print(a[i][j], end = " ")
      else:
        print(a[i][k], end=' ')
        k = k - 1
    print()

alternate(mat)
    
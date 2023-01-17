# Python program to copy upper triangle to lower triangle in python.

# Matrix


#     1   2   3         1    2    3
#     4   5   6         2    5    6
#     7   8   9         3    6    9

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(matrix)):
#   for j in range(len(matrix[0])):
#     print(matrix[i][j], end=" ")
#   print()


def copy_upper(a):
  b = []
  for i in range(len(a)):
    c=[]
    for j in range(len(a[0])):
      if i > j:
        c.append(a[j][i])
      else:
        c.append(a[i][j])
    b.append(c)

  for i in range(len(b)):
    for j in range(len(b[0])):
      print(b[i][j], end=" ")
    print()

copy_upper(matrix)
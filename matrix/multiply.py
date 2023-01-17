# python program to multiply row with column

#   1   2   3            1     2     3
#   4   5   6            4     5     6
#   7   8   9            7     8     9

#  1*1 + 2*4 + 3*7 = 1 + 8 + 21 = 30
#  1*2 + 2*5 + 3*8 = 2 + 10 + 24 = 36
#  1*3 + 2*6 + 3*9 = 3 + 12 + 27 = 42


mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]

def multiply(a, b):
  sum = 0
  bc = []
  for i in range(len(a)):
    c = []
    k = 0
    while k < len(a):
      for j in range(len(a[0])):
        sum += a[i][j] * b[j][k]
      c.append(sum)
      print(sum)
      sum = 0
      k = k + 1
    bc.append(c)
  
  print(bc)

  # for i in range(len(bc)):
  #   for j in range(len(bc[0])):
  #     print(bc[i][j], end = ' ')
  #   print()

multiply(mat1, mat2)
      



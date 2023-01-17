# pyhton progrm to find the sum of each row and each column of a matrix.

                          # row sum
#           1    2     3     6
#           4    5     6     15
#           7    8     9     24
# col sum  12   15    18

mat = [[1,2,3],[4,5,6],[7,8,9]]

def sum_of_rc(a):
  r = []
  c = []
  for i in range(len(a)):
    sumr = 0
    sumc = 0
    for j in range(len(a[0])):
      sumr += a[i][j]
      sumc += a[j][i]
    
    r.append(sumr)
    c.append(sumc)

  for i in range(len(a)):
    for j in range(len(a[0])):
      print(a[i][j], end='  ')
    print(r[i])

  for i in c:
    print(i, end=' ')
  print()

    

sum_of_rc(mat)

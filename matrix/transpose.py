# transpose a matrix

#   matrix            transpose
# 1   2   3            1    4   7
# 4   5   6            2    5   8
# 7   8   9            3    6   9

mat = [[1,2,3],[4,5,6],[7,8,9]]

def transpose(a):
  for i in range(len(a)):
    for j in range(len(a[0])):
      print(a[j][i], end=' ')
    print()

print(mat)
print(30 * '--')
transpose(mat)

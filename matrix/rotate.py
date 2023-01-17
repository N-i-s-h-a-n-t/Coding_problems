# rotate matrix 90 anticlockwise

# matrix              transpose         roatate 90 anticlockwise
  
                # (convert row to column)

#   1   2   3         1   4   7           3   6   9
#   4   5   6         2   5   8           2   5   8
#   7   8   9         3   6   9           1   4   7

m = int(input("Enter no of rows  "))
n = int(input("Enter no of clumns  "))
a = []
for i in range(m):
  b = []
  for j in range(n):
    j = int(input(f"enter no in pocket [{i}][{j}] "))
    b.append(j)

  a.append(b)
print("matrix is ....")
for i in range(m):
  for j in range(n):
    print(a[i][j], end=" ")
  print()

print(30 * '-')

def anticlock(a):
  b = []
  for i in range(len(a)):
    c = []
    for j in range(len(a[0])):
        c.append(a[j][i])
    b.append(c)
  
  for i in range(len(b)-1, -1, -1):
    for j in range(len(b[0])):
      print(b[i][j], end =" ")
    print()

anticlock(a)

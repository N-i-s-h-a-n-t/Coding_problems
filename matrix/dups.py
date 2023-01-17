# Python program to find duplicate rows in a binary matrix

#     1 0 0 1 0         18
#     0 1 1 0 0         12
#     1 0 0 1 0         18
#     0 0 1 1 0          6
#     0 1 1 0 0         12


mat = [[1,0,0,1,0],[0,1,1,0,0],[1,0,0,1,0],[0,0,1,1,0],[0,1,1,0,0]]

def bin_to_dec(n):
  des = 0
  base = 1
  while n != 0:
    rem = n % 10
    des = des + rem * base
    base = base * 2
    n = int(n / 10)
  return des



dic = {}
for i in range(len(mat)):
  res = 0
  for j in range(len(mat[i])):
      res = res * 10 + mat[i][j]
  dic[i] = bin_to_dec(res)
  # dic[i] = res

l = []
f = 0
for key, value in dic.items():
  if value not in l:
    l.append(value)
  else:
    print("Duplicate found in "+ str(key+1))
    f = 1

if f == 0:
  print("not found duplicate row")

print(dic)
    

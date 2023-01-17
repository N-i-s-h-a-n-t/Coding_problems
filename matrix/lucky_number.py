l = [
  [1,10,4,2],
  [9,3,8,7],
  [15,16,17,12]
  ]

# l = [
#   [3,7,8],
#   [9,11,13],
#   [15,16,17]]

l =[[7,8],[1,2]]

def lucky_number(a):
  l = []
  for i in range(len(a)):
    min = a[i][0]
    pair = []
    pair.append(i)
    pair.append(0)
    
    for j in range(len(a[0])):
      if min > a[i][j]:
        min = a[i][j]
        pair.append(i)
        pair.append(j)

    max = 0
    if pair == []:
      for i in range(len(a)):
        if max < a[i][0]:
          max = a[i][0]
    
    elif pair != []:
      i = pair[-1]
      for  j in range(len(a)):
        if max < a[j][i]:
          max = a[j][i]

    if min == max:
      return min

print(f"Lucky number is {lucky_number(l)}")
# to convert a umber from decimal to binary using recursion

def dtb(a):
  if a // 2 == 0:
    return '1'
  else:
    return dtb(a//2) + str(a%2)

print(dtb(13))
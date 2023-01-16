# Permutation

# example   keap - peak
#           rail - liar


def permutation(list1, list2):
  if len(list1) != len(list2):
    return False
  else:
    for i in list1:
      if i in list2:
        continue
      else:
        return False

  return True


list1 = ['l','i','a','r']
list2 = ['r','s','a','l']
print(permutation(list1, list2))
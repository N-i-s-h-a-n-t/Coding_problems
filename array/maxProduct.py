# How to find maximum product of two integers in the array where all elements
# are positive

myArray = [1, 20, 30, 44, 56, 87, 65, 34, 48]


def maxProduct(array):
  maxProduct = 0
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[i] * array[j] > maxProduct:
        maxProduct = array[i] * array[j]
        pairs = f"[{array[i]}, {array[j]}]"

  return maxProduct, pairs

print(maxProduct(myArray))
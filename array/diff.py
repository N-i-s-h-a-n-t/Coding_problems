#  Difference Between Element Sum and Digit Sum of an Array

# Example 1:

# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Explanation:
# The element sum of nums is 1 + 2 + 3 + 4 = 10.
# The digit sum of nums is 1 + 2 + 3 + 4 = 10.
# The absolute difference between the element sum and digit sum is |10 - 10| = 0.

def sums(number):
  if number == 0 or number == 1:
    return number
  else:
    return int(number%10) + sums(int(number/10))


def difference(nums):
  digitsum = 0
  summ = 0 
  for i in nums:
    summ += i
    if i > 9:
      digitsum  += sums(i)
    else:
      digitsum += i

  return summ - digitsum

print(difference([1,2,3,4]))
      



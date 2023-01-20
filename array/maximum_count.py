# Maximum Count of Positive Integer and Negative Integer

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

def count(nums):
  neg = 0
  pos = 0
  for i in nums:
    if i < 0:
      neg += 1
    if i > 0:
      pos += 1

  return pos if pos > neg else neg

print(count([-3,-2,-1,0,0,1,2]))
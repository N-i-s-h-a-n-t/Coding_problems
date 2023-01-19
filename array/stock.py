#  Best Time to Buy and Sell Stock

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are 
# done and the max profit = 0.

prices = [2, 4, 1]
def sell(a):
  left = 0
  right = 1
  max_profit = 0
  while right < len(a):
    current_profit = a[right] - a[left]
    if a[left] < a[right]:
      max_profit = max(current_profit, max_profit)
    else:
      left = right
    right += 1
  return max_profit

sell(prices)
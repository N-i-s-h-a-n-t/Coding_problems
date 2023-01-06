# how to find the sum of digits of a positive integer

def sum_of_digit(number):
  if number <= 9:
    return number
  else:
    return number % 10 + sum_of_digit(number // 10)

print(sum_of_digit(1543))
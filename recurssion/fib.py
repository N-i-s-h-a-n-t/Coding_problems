# Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence

def fib(num):
  if num == 0 or num == 1:
    return num
  else:
    return  fib(num-1) + fib(num-2)

print(fib(4))
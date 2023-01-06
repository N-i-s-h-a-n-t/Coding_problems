# to find GCD(greatest COmmon Divisor) of two numbers using recurssion

# euclidean algorithm
# gcd(48, 18)
# step 1 : 48/18 = 2 remainder 12
# step 2: 18/12 = 1 remainder 6
# step 3: 12/6 = 2 remainder 0

def gcd(a, b):
  if a%b == 0:
    return b
  else:
    return gcd(b, a%b)

print(gcd(48, 18))
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output

# 200
# Explanation

# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned =  55 + 45 + 40 + 60 = 200


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

s = input()
size = list(map(int, input().split()))
a = Counter(size)
n = input()
sum = 0
mydict = {1:1, 3:2}
for i in range(int(n)):
    c = list(map(int, input().split()))
    if c[0] in a:
        if a[c[0]] != 0:
            a[c[0]] = a[c[0]]-1
            sum = sum + c[1]
            
print(sum)

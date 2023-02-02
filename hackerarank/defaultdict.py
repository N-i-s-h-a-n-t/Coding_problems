# Sample Input

# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b
# Sample Output

# 1 2 4
# 3 5


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
B = []

for n in range(n):
    A[input()].append(n+1)

for m in range(m):
    B.append(input())


for b in B:
    if b in A:
        print(*A[b])
    else:
        print(-1)

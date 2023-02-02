# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]


from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(product(a, b))
res = ''
for x in c:
    res += str(x) + ' '
    
print(res)
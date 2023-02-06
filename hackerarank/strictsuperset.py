# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

# Sample Input 0

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Sample Output 0

# False
# Explanation 0

# Set A is the strict superset of the set([1, 2, 3, 4, 5]) but not of the set([100, 11, 12]) because 100 is not in set .
# Hence, the output is False.

setA = set(map(int, input().split()))
res = False  

for _ in range(int(input())):
    setB = set(map(int, input().split()))
    if len(setA) == len(setB):
        res = False
        break
    elif setB.difference(setA):
        res = False
        break
    else:
        res = True
        continue
        
print(res)
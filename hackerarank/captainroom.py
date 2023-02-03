# → An unknown group of families consisting of k members per group where  k≠1 .

# Output Format

# Output the Captain's room number.

# Sample Input

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
# Sample Output

# 8
# Explanation

# The list of room numbers contains 31 elements. Since k is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8.
# Hence, 8 is the Captain's room number.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
family = input()
myset = list(map(int, input().split()))
c = Counter(myset)
for k,v in c.items():
    if v == 1:
        print(k)
# Sample Input

# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3
# Sample Output

# AB
# CA
# AD

# t0 = 'AAB' --> u0 = 'AB'
# t1 = 'CAA' --> u1 = 'CA'
# t3 = 'ADA' --> u2='AD'


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        print(''.join(set(string[i:i + k])))


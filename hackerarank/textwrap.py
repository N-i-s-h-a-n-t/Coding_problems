# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    res = ''
    x = textwrap.wrap(string, width = max_width)
    for i in range(len(x)):
        res += x[i]+'\n'
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
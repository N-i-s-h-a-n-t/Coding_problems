# Sample Input

# chris alan
# Sample Output

# Chris Alan

def solve(s):
    for i in range(len(s)):
        if i == 0:
            if ord(s[i]) >96 and ord(s[i]) < 123:
                s = chr(ord(s[i]) - 32) + s[i+1:]
        elif s[i] == ' ':
            if ord(s[i+1]) >96 and ord(s[i+1]) < 123:
                s = s[:i+1] + chr(ord(s[i+1:i+2]) - 32) + s[i+2:]
    return s


print(solve('chris alan'))
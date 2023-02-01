# n the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True




def func1(s):
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >=  48 and ord(s[i]) <= 57) :
            return True
    return False

def func2(s):
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
            return True
    return False
    
def func3(s):
    for i in range(len(s)):
        if (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            return True
    return False
    
def func4(s):
    for i in range(len(s)):
        if (ord(s[i]) >= 97 and ord(s[i]) <= 122):
            return True
    return False
    
def func5(s):
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            return True
    return False

def func(s):
    print(func1(s))
    print(func2(s))
    print(func3(s))
    print(func4(s))
    print(func5(s))
    
if __name__ == '__main__':
    s = input()
    func(s)
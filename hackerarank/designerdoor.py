# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------



n, c = input().split()
n = int(n)
j = 1
for i in range(1, n + 1):
    if (n // 2 + 1) == i:
        print('WELCOME'.center(n * 3, '-'))
    else:
        if i < (n // 2 + 1):
            ans = '.|.' * j
            print(ans.center(n*3,'-'))
            j = j + 2
        else:
            j  = j - 2
            ans = '.|.' * j
            print(ans.center(n*3,'-'))

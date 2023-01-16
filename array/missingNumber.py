# how to find the missing number in an integer of 1 to 20.

# 1 + 2 + 3 .... + n = n(n+1)/2

mylist = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def findMissing(mylist, n):
    sum = 0
    for i in mylist:
      sum += i

    res = int(n * (n+1)/2) - sum
    print(f"Missing Number is {res}.")

findMissing(mylist, 20)
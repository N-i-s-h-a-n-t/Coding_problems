# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry


if __name__ == '__main__':
    records = []
    n = input()
    for _ in range(int(n)):
        c = []
        a = str(input())
        c.append(a)
        b = float(input())
        c.append(b)
        records.append(c)

    l = []
    for i in range(len(records)):
        l.append(records[i][1])
    
    see_another = min(l)
    l.remove(min(l))
    while True:
        if see_another in l:
            l.remove(min(l))
        else:
            break
    mins = min(l)
    names = []
    for i in range(len(records)):
        if mins == records[i][1]:
            names.append(records[i][0])
        
    names.sort()
    for x in names:
        print(x)

# write a program to find all pairs of integers whose sum is equal to given number

inp = [1, 2, 3, 2, 4, 5 ,2,  6, 3 , 9, 11]
target = 6

def pairsum(inp, target):
  for i in range(len(inp)):
    for j in range(i+1, len(inp)):
      if inp[i] == inp[j]:
        continue
      elif inp[i] + inp[j] == target:
        print(f"[{i}, {j}]")

pairsum(inp, target)
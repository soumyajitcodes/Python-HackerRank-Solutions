from itertools import combinations
n = int(input())
d = input().split()
k = int(input())

c = 0
t = 0
for i in combinations(d, k):
    if "a" in i:
        c += 1
    t += 1

print(c/t)
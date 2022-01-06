from itertools import permutations
a, k = input().split()
a = sorted(a)
k = int(k)
l = permutations(a, k)
for i in l:
    c = ''
    for j in i:
        c += j
    print(c)
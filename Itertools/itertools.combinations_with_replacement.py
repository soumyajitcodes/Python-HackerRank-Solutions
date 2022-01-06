from itertools import combinations_with_replacement
a, k = input().split()
a = sorted(a)
k = int(k)
l = combinations_with_replacement(a, k)
for i in l:
    c = ''
    for j in i:
        c += j
    print(c)
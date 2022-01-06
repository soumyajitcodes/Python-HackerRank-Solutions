n = int(input())
A = [int(i) for i in input().split()[:n]]
large, slarge = 0, 0
for i in A:
    if i > large:
        large, slarge = i, large
    elif i < large and i > slarge:
        slarge = i
print(slarge)
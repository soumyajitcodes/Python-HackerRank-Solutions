n = int(input())
A = set(int(x) for x in input().split())
N = int(input())
while N:
    op, a = input().split()
    c = set(int(x) for x in input().split())
    if op == 'update':
        A |= c
    elif op == "intersection_update":
        A &= c
    elif op == "difference_update":
        A -= c
    elif op == "symmetric_difference_update":
        A ^= c
    N -= 1

print(sum(A))
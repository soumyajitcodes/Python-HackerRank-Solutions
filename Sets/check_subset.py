T = int(input())
while T:
    A = int(input())
    A_set = set(int(x) for x in input().split())
    B = int(input())
    B_set = set(int(x) for x in input().split())
    print(A_set.issubset(B_set))
    T -= 1
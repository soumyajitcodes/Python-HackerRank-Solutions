n = int(input())
n_arr = set(map(int, input().split()[:n]))
b = int(input())
b_arr = set(map(int, input().split()[:n]))
print(len(n_arr.symmetric_difference(b_arr)))
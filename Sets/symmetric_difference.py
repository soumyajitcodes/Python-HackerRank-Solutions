M = int(input())
M_list = [int(i) for i in input().split()[:M]]

N = int(input())
N_list = [int(i) for i in input().split()[:N]]

M_set = set(M_list)
N_set = set(N_list)

tmp_set1 = M_set.difference(N_set)
tmp_set2 = N_set.difference(M_set)

result_set = tmp_set1.union(tmp_set2)
result_set = sorted(result_set)
for i in result_set:
    print(i)
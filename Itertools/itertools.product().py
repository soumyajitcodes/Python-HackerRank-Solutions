from itertools import product


def get_product(a, b):
    return product(a, b)


a = set(map(int, input().split()))
b = set(int(i) for i in input().split())
res = list(get_product(a, b))
for i in res:
    print(i, end=' ')
